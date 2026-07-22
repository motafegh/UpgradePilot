# When Something Felt Off Again

*How a small release-note extractor reopened an old Sentinel lesson and changed the direction of UpgradePilot.*

**July 22–23, 2026**

## What I Thought I Understood

When I began this session, I did understand one part of UpgradePilot.

I understood that the project would receive some form of input, normalize it, validate it, and prepare it for the next process. We had already used Pydantic, customized configurations, and strict schemas for that boundary. I could recognize the expected input types, understand why undeclared fields should be rejected, and see how raw information could be turned into a controlled structure before anything else relied on it.

In my mind, the beginning looked roughly like this:

```text
input
→ normalization
→ validation
→ trusted structured record
→ next process
```

That local picture made sense to me.

What I did not understand was the complete runtime surrounding it.

I did not have a clear picture of what would start an UpgradePilot run, who or what would provide the initial input, which information would arrive immediately, which evidence the system would have to discover later, how those items would be investigated, or what the maintainer would finally receive. I understood some pieces, but I could not yet see the whole machine.

Still, I continued the M2 work that had started the previous night. I hoped that the larger picture might become clearer while the implementation progressed.

## A Small Extractor

One part of the work involved using a local large language model as a release-note extractor.

The idea appeared bounded and understandable. The model would receive text such as a release note saying that support for Python 3.8 had been dropped, and it would return a predefined structured JSON result.

We were using LM Studio with Qwen 3 4B and a small Gemma model. The AI assistant was writing the code, running the tests, comparing the models, documenting their performance, and trying to keep me onboarded while I read documents produced during the previous session.

At first, I was interested.

Adversarial testing was new to me, and I was learning from it. I was also curious about why these models were failing at what appeared to be a simple extraction task.

Then the work began to widen.

## The Second Model

The models could not completely pass the adversarial tests.

The discussion then moved toward using another LLM to inspect or protect the input of the first LLM—a second model acting as a control around the first one. I suggested or accepted that direction, and the AI assistant implemented it.

At the same time, the assistant explained that the underlying problem could not be solved completely. The extracted result would still have to be treated as model-derived, uncertain, or limited in authority.

That combination disturbed me.

We were adding another intelligent component to control the first intelligent component, while also admitting that the result could never become fully trustworthy. If the output would remain explicitly uncertain, why were we constructing so much machinery around this one transformation?

I had not inspected all the implementation details or every adversarial test myself. I had only asked the assistant to explain briefly what was failing and how it was trying to deal with those failures.

I could also see the opposite risk. A detector designed to catch adversarial text might classify normal text as adversarial. While trying to prevent one failure, we could introduce false positives and create another problem for ourselves.

I did not know whether my technical interpretation was fully correct.

I only knew that something felt off.

## Sentinel's Shadow

The feeling was familiar because of Sentinel.

In Sentinel, the fundamental problem was the data and its labels, but neither I nor the AI assistants recognized that early enough. We kept treating the visible problem as a machine-learning model problem.

We changed model approaches. We added new graphs and extraction methods. We optimized models and trained them on incorrectly labelled data. One training run could take three or four days. When the resulting metrics were poor, we returned to model optimization, modified the extraction process, trained again, waited several more days, and received another poor result.

The loop repeated many times. Sentinel eventually accumulated at least eleven model versions.

The work was not useless. I learned many techniques, model approaches, and ways of thinking. I could have learned those same things after correcting the data problem. But because the root problem remained hidden, the project entered a local optimization trap: each attempt improved or changed the machinery around the problem without resolving the problem itself.

Even later work on the data module did not immediately fix the situation because we still were not examining the correct things in the correct way.

Sentinel left me with one important form of experience.

I now become suspicious earlier.

I begin to notice when we may be travelling too far, when the real problem may exist somewhere else, when complexity is growing faster than understanding, or when we are investing heavily in a responsibility that may not even be necessary.

I may not yet know what is wrong. I may not have the vocabulary or technical explanation ready. But I recognize the shape of the pattern faster.

That pattern was appearing again around the release-note extractor.

## Was I Missing the Project?

My first reaction was not that the project was wrong.

My first reaction was that I might be missing something.

Perhaps the thesis, charter, or another specification had already assigned UpgradePilot a responsibility that justified all this adversarial protection. Perhaps the project really was supposed to defend itself against compromised upstream text at this stage. Perhaps I simply did not understand the main goal well enough.

The project had intentionally delayed many details until the point where they became necessary. That approach prevented premature design, but it also meant that I had never formed a complete real-world runtime picture from beginning to end.

I understood the input contract. I did not understand the full journey of the input.

I knew how a value might be normalized and validated. I did not know who originally produced it, how UpgradePilot acquired it, what authority it should receive, what other evidence surrounded it, or how an error would propagate into a maintainer decision.

Before challenging the implementation, I asked the AI assistant to explain the project goal and what was actually happening.

Then I started pushing back.

## Three Questions

The first question was about consequence.

> What was the worst thing that could realistically happen if the most dangerous adversarial instruction passed through a release note and the system failed to detect it?

At this stage, the LLM was receiving a piece of text and filling fields in a structured JSON object.

What did that model actually have access to? Did it have passwords? Could it execute files? Could it run commands? Could it directly control anything?

My rough understanding was that the immediate failure might be much smaller: the model could populate an evidence field incorrectly, omit something important, or produce a wrong interpretation. That could still influence downstream reasoning, but it was not the same threat as giving an agent credentials, tools, or arbitrary execution access.

The second question was about origin.

> Where did this release note come from in the first place?

Who produced all the other input and evidence items? Which sources did we trust, and what did “trust” mean here? If we believed a source was too untrustworthy to consume, why were we collecting information from it at all?

If an upstream project or another source could be compromised, why were we focusing so heavily on adversarial text inside one release-note item while every other source could also contain incorrect, manipulated, stale, or misleading information?

The third question was about responsibility.

> What was UpgradePilot actually responsible for?

Was UpgradePilot supposed to ensure that upstream sources could never be compromised? Was it supposed to prove every supplied item true before using it? Or was its role to receive and acquire observations, preserve where they came from, investigate what they could support, compare them with other evidence, and assemble a bounded picture for the maintainer?

I did not begin with that complete theory. I reached toward it through the questions.

At first, all I had was the feeling that something was wrong and the suspicion that I did not understand the actual product.

## The Answers That Did Not Settle It

The assistant's answers did not resolve the concern.

They included phrases such as “if,” “maybe,” and “if the origin somehow becomes compromised.” The answer explained how an adversarial release note might exist, but it did not adequately explain the origins, authority, or failure behavior of the other inputs.

I pushed back again.

> If the sources could be compromised, what about every other item?

The assistant replied that those other items could also be compromised.

At that point, I stopped reading the rest closely.

The explanation of where inputs came from involved examples such as a library being updated and Dependabot producing an update event. The sources were also described as generally reliable. To me, this created a conflict: we were treating one item as dangerous enough to justify layers of adversarial controls, while also describing its surrounding ecosystem as the normal source of the evidence the product depended on.

Maybe there was a technically valid answer. But we did not appear to share a concrete model of the complete runtime or its actual threat boundaries.

The work had become locally sophisticated while the global picture remained unclear.

## Breaking the Loop

I asked the assistant to preserve and document everything we had done in the extraction and adversarial-testing work.

Then I stopped the session.

That stop mattered.

In Sentinel, we often responded to a poor result by adding another model, another feature, another extraction method, or another training run. This time, before another technical loop could establish itself, I interrupted it.

I opened a new conversation and brought the questions there.

That conversation exposed that the uncertainty was not limited to Qwen, Gemma, adversarial detection, or release-note extraction. We lacked a real, shared picture of what starts an UpgradePilot run, what information it initially receives, what must be discovered later, who produces each item, what each item can establish, what happens when information is missing or wrong, how the complete investigation works, and what the maintainer finally receives.

We had been implementing one narrow responsibility without first experiencing the whole product.

This was not only a model-selection problem.

It was a missing-runtime-picture problem.

## Building a Reality Anchor

That realization led to the separate `product-simulation/` workspace.

Instead of immediately implementing more of UpgradePilot, the AI assistant and I would manually act as the complete system for real dependency-update cases.

We would begin from a real event, identify the exact case, collect evidence, preserve its origins and limitations, perform the investigation, reason under uncertainty, and produce the result a maintainer might actually need.

The simulation became a reality anchor: a place where an abstract plan could be compared against real inputs, real repositories, real evidence gaps, real failure modes, and real maintainer decisions.

I did not personally read every new specification or artifact as it was created. The AI assistant still performed most of the technical acquisition, artifact construction, and documentation. But I monitored and directed the work through three different real cases.

Even the simulation did not arrive in its current form immediately.

After seeing how the first cases were represented, I changed the specifications again. Those changes led to the current structure, where the complete human-readable case story exists alongside the individual runtime artifacts that the imagined system would create and update during its work.

Now there are three full real examples.

## What I Know Now—and What I Still Do Not

I still do not fully know what all the simulation findings mean for the original plans.

I know that the written plans now conflict with things discovered through `product-simulation/`, and that those plans will need to be examined and changed. I do not yet know exactly what must change, why every change is necessary, or how the corrected route should look.

But I now have something concrete to return to.

When the project begins feeling abstract, overcomplicated, or detached from the problem it is supposed to solve, the simplest response is to compare it with a real case and manually perform the real work.

Instead of continuing to build around an unclear assumption, I can return to the actual input, the actual environment, the actual investigation, and the actual user need.

The same feeling may happen again. I may once again be unable to explain immediately what is wrong.

When it does, I do not want to ignore it or assume that the specifications and the AI must understand the project better than I do. I want to stop, inspect reality, challenge the assumptions, and discover what the project is actually supposed to do before another technical loop grows around the wrong problem.

That instinct came from Sentinel.

This time, I noticed it earlier.
