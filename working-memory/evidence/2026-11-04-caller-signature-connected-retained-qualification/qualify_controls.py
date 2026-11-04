"""Run separately labelled protocol and retained-code rejection fixture pressures."""
from hashlib import sha256
import argparse
import json
from pathlib import Path

from control_cases import glyphslib_control, rejection_control
from retained_cases import selected_cases
from qualify import ROOT, HERE, execute
from upgradepilot.caller_signature.acquisition import AcquisitionPolicy
from upgradepilot.caller_signature.result_codec import encode_analysis_input
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.caller_signature_delivery import open_caller_signature_checkpoint


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(mode=0o700,parents=True,exist_ok=False)
    glyph=next(c for c in selected_cases(ROOT) if c.name=='glyphslib-protocol')
    cases=[glyphslib_control(glyph),rejection_control(ROOT)]
    methods={str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest()
             for p in [*sorted((ROOT/'src/upgradepilot').rglob('*.py')),*sorted(HERE.glob('*.py'))]}
    (args.output/'contract.json').write_text(json.dumps(dict(proof='explicit_authored_controls_not_historical_admission',
        controls=[note for _,note in cases],method_sha256=methods,criteria={
            'protocol':'paired native witness with complete ordered allocation/attribute_getter/factory_return/call_protocol and original premises',
            'rejection':'paired root with old bound and proposed app keyword not received from retained HTTPX declaration'},
        source_bounds='Current ordinary profile, no selectors or cap enlargement.'),indent=2)+'\n')
    results=[]
    for case,note in cases:
        row=execute(case,'http',args.output/case.name,controlled=True)
        row['control_provenance']=note
        if row.get('confirmed_revision'):
            opened=open_caller_signature_checkpoint(CheckpointStore.open(args.output/case.name/'store',read_only=True),row['confirmed_revision'])
            run=opened.native.comparison
            candidates=run.result.candidates if run and run.result else ()
            if 'protocol' in case.name:
                operations=('allocation','attribute_getter','factory_return','call_protocol')
                found=[]
                for candidate in candidates:
                    steps=[s.operation for s in candidate.steps]
                    if all(op in steps for op in operations):
                        assert [steps.index(op) for op in operations]==sorted(steps.index(op) for op in operations)
                        found.append(dict(role=candidate.callee_role.role,outcome=candidate.comparison.outcome,
                                          operations=steps,premises=candidate.premises))
                row['protocol_witnesses']=found
                row['pressure_pass']=bool(found) and row.get('positive_pair_qualification',False)
            else:
                rejected=[c for c in candidates if c.callee_role.role=='proposed_dependency' and c.comparison.outcome=='rejected'
                          and any(k.name=='app' and k.outcome=='not_received' for k in c.comparison.keyword_reception)]
                row['proposed_app_rejections']=len(rejected)
                row['pressure_pass']=bool(rejected) and any(c.callee_role.role=='old_dependency' and c.comparison.outcome=='bound'
                    and c.root_call_id in {r.root_call_id for r in rejected} for c in candidates)
        results.append(row)
        (args.output/'results.json').write_text(json.dumps(results,indent=2)+'\n')
        print(json.dumps(row),flush=True)
    assert methods=={name:sha256((ROOT/name).read_bytes()).hexdigest() for name in methods}


if __name__=='__main__':
    main()
