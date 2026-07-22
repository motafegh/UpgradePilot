# When Something Felt Off Again

**July 22–23, 2026**

Today I was continuing the M2 work that had started the previous night.

I was not confident that I understood the project properly. I did not have a clear picture of the complete UpgradePilot runtime, what exactly would enter the system, where those inputs would come from, or even what the real goal of the work in front of me was. I knew we were working with evidence items, and I hoped that by continuing I might understand the larger picture while the implementation progressed.

One part of the work involved using a local large language model as a release-note extractor. The idea was that the model would receive text such as a release note saying that support for Python 3.8 had been dropped, and it would return a predefined structured JSON result.

We were using LM Studio with Qwen 3 4B and a small Gemma model. The AI assistant was writing the code, running the tests, comparing the models, documenting their performance, and trying to keep me onboarded while I read some of the documents produced during the previous session.

At first, I was interested. Adversarial testing was a new concept for me, and I was learning from it. I also started wondering why these models were failing at what appeared to be a simple extraction task.

The work kept expanding.

The models could not completely pass the adversarial tests. Then the discussion moved toward using another LLM to inspect or protect the input of the first LLM. I suggested or accepted that direction, and the AI assistant implemented it. At the same time, it explained that the problem could not be solved completely and that the results would still be marked as model-derived or uncertain in some way.

That was when the process began to feel wrong.

I had not inspected the implementation details or all the tests myself. I had only asked the assistant to explain briefly what was failing and how it was trying to address those failures. I could also see another side of the controls we were adding: while trying to detect adversarial text, the system could classify normal text as adversarial. It felt as though we might be inventing another problem while trying to solve the first one.

I was not certain that this interpretation was technically correct. I only knew that something felt off.

The feeling was familiar because of Sentinel.

In Sentinel, the fundamental problem was the data and its labels, but neither I nor the AI assistants recognized that early enough. We kept treating the visible problem as an ML model problem.

We changed model approaches. We added new graphs and extraction methods. We optimized models and trained them on incorrectly labelled data. A training run could take three or four days. When the resulting metrics were poor, we returned to model optimization, changed the extraction process, trained again, waited several more days, and received another poor result.

This loop happened many times. Sentinel eventually accumulated at least eleven model versions.

I learned many useful methods during that process, and I could have learned those same things after correcting the data problem. But the central issue remained unresolved while large amounts of work accumulated around it. Even the later data-module work did not immediately fix the real problem because we still were not examining the correct things in the correct way.

That experience left me with something valuable: I now become suspicious earlier.

I begin to notice when we may be travelling too far, when the real problem may be somewhere else, when we are overcomplicating something, or when we are investing heavily in a responsibility that may not even be necessary. I may not yet know exactly what is wrong, but I recognize the pattern faster.

That was the feeling I had during the release-note extractor work.

I first assumed that perhaps I simply did not understand the project well enough. Maybe the thesis, charter, or another specification had already assigned UpgradePilot a responsibility that justified everything we were doing. Because the project had intentionally delayed many details until the moment they were needed, I had never formed a complete real-world picture of the system from beginning to end.

I did not know what the product would receive when a run started. I did not know which information was initially supplied and which information the product would later acquire. I had not seen the full investigation happen in reality. I was therefore not sure whether I was identifying a genuine problem or merely missing an important part of the design.

Before challenging the work, I asked the AI assistant to explain the project goal and what was actually happening.

Then I started asking more direct questions.

What was the worst thing that could realistically happen if the most dangerous adversarial instruction passed through a release note and the system failed to detect it?

At this stage, the LLM was receiving a piece of text and filling fields in a structured JSON object. What did that model actually have access to? Did it have passwords? Could it execute files? Could it run commands? Could it directly control anything?

My rough understanding was that the immediate failure might be much smaller: it could populate an evidence field incorrectly, omit something, or produce a wrong interpretation. That could still matter downstream, but it was not the same threat as giving an agent credentials, tools, or arbitrary execution access.

Then another question appeared.

Where did this release note come from in the first place?

Who produced all the other input and evidence items? Which sources did we trust, and in what sense did we trust them? If we believed a source was too untrustworthy to consume, why were we collecting information from it at all? If an upstream project or another source could be compromised, why were we focusing so heavily on adversarial text in one release-note item while the other evidence sources might also contain wrong or manipulated information?

Then I questioned the project responsibility itself.

Was UpgradePilot supposed to ensure that upstream sources could never be compromised? Was it supposed to prove every supplied item true? Or was its job to receive and acquire different observations, preserve where they came from, investigate what they could support, compare them with other evidence, and gradually assemble a bounded picture for the maintainer?

I did not begin with that complete theory. I began only with the feeling that something was wrong and that I did not understand the actual product.

The assistant’s answers did not settle the concern. They included phrases such as “if,” “maybe,” or “if the origin somehow becomes compromised.” The answer discussed the possibility of an adversarial release note but did not adequately explain the origins and risks of the other input items.

I pushed back again.

If the sources could be compromised, what about every other item?

The assistant replied that those other items could also be compromised. At that point I stopped reading the rest closely. The explanation of where inputs came from involved examples such as a library being updated and Dependabot creating something, but I no longer trusted that we had a shared, concrete picture of the complete runtime.

I asked the assistant to preserve and document everything we had done in the extraction and adversarial-testing work. Then I stopped the session.

I opened a new conversation and brought the questions there.

That conversation exposed that the uncertainty was not limited to the choice of model or the quality of the extractor. We lacked a real, shared picture of what starts an UpgradePilot run, what information it initially receives, what must be discovered later, who produces each item, what each item can establish, what happens when information is missing or wrong, how the complete investigation works, and what the maintainer finally receives.

We had been implementing one narrow responsibility without first experiencing the whole product.

That led to a separate `product-simulation/` workspace.

Instead of immediately implementing more of UpgradePilot, the AI assistant and I would manually act as the complete system for real dependency-update cases. We would begin from a real event, identify the exact case, collect evidence, preserve its origins and limitations, perform the investigation, reason under uncertainty, and produce the result a maintainer might actually need.

I did not read every new specification or artifact as it was created. The AI assistant still performed most of the technical acquisition, construction, and documentation. But I monitored and directed the work through three different real cases.

Even that simulation did not arrive in its current form immediately. After seeing how the first cases were represented, I changed the specifications again. Those changes led to the present structure, where the complete human-readable case story exists alongside the individual runtime artifacts that the imagined system would create and update during its work.

Now there are three full real examples.

I still do not fully know what all of their findings mean for the original plans. I know that the written plans now conflict with things discovered through `product-simulation/`, and that the plans will need to be examined and changed. I do not yet know exactly what must change, why each change is necessary, or how the corrected route should look.

But I now have something concrete to return to.

When the project begins feeling abstract, overcomplicated, or detached from the problem it is supposed to solve, the simplest response is to compare it with a real case and manually perform the real work. Instead of continuing to build around an unclear assumption, I can return to the actual input, the actual environment, the actual investigation, and the actual user need.

The same feeling may happen again. I may once again be unable to explain immediately what is wrong.

When it does, I do not want to ignore it or assume that the specifications and the AI must understand the project better than I do. I want to stop, inspect the real situation, challenge the assumptions, and find out what the project is actually supposed to do before allowing another technical loop to grow around the wrong problem.

That instinct came from Sentinel.

This time, I noticed it earlier.
