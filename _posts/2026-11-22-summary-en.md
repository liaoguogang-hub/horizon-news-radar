---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 141 items, 43 important content pieces were selected

---

1. [Perplexity as a Signal of Model Intelligence](#item-1) ⭐️ 8.0/10
2. [Anthropic’s 2028 Power Mix Is Mostly Gas and Coal](#item-2) ⭐️ 8.0/10
3. [Inkling-2-Mini Runs in 5.4 GB at 150 Tokens per Second](#item-3) ⭐️ 8.0/10
4. [OpenRouter Removes Providers After Prompt Privacy Incidents](#item-4) ⭐️ 8.0/10
5. [Japanese Automakers Standardize Parts to Cut Costs](#item-5) ⭐️ 7.0/10
6. [Show HN: A Game Where You Are an LLM Subagent](#item-6) ⭐️ 7.0/10
7. [Alliance Proposes Open Protocol for Social Media](#item-7) ⭐️ 7.0/10
8. [Delta Flights Delayed After Atlanta Weight-and-Balance System Outage](#item-8) ⭐️ 7.0/10
9. [Muru Brings Rust-Powered Python Serving to ASGI and WSGI](#item-9) ⭐️ 7.0/10
10. [Two Million AI Canary Tokens Expose Supply-Chain Privacy Failures](#item-10) ⭐️ 7.0/10
11. [Packaging PostgreSQL as a Single Binary](#item-11) ⭐️ 7.0/10
12. [Microsoft 365 Outage Post-Incident Report Explains Root Cause](#item-12) ⭐️ 7.0/10
13. [Signal Restricts Mobile Screenshots Over AI Surveillance Concerns](#item-13) ⭐️ 7.0/10
14. [Race Realism Fails Modern Genetics](#item-14) ⭐️ 7.0/10
15. [FCC Blocks California’s AT&amp;T Home Phone Rules](#item-15) ⭐️ 7.0/10
16. [Banks Restrict Third-Party AI Agents and Shift Liability](#item-16) ⭐️ 7.0/10
17. [Telltale Reads Back QNX 8.0 Instrument Pixels to Catch False Displays](#item-17) ⭐️ 7.0/10
18. [Answer Receipts Make Text-to-SQL Results Auditable](#item-18) ⭐️ 7.0/10
19. [Silicon Valley’s Shift From Innovation to Financialization](#item-19) ⭐️ 6.0/10
20. [Sandwich Simulator Turns Layering Into Playful Web Interaction](#item-20) ⭐️ 6.0/10
21. [Backblaze Users Question Updated Data Sale and Sharing Terms](#item-21) ⭐️ 6.0/10
22. [Has Software Always Been Too Complex for Humans?](#item-22) ⭐️ 6.0/10
23. [C++26 Technical Work Completed After Second Review](#item-23) ⭐️ 6.0/10
24. [Mathematicians React to a Future AI Proof of GRH](#item-24) ⭐️ 6.0/10
25. [NixOS Bring-Up on Alibaba RISC-V Board](#item-25) ⭐️ 6.0/10
26. [Monitor Reportedly Cut Download Speed by 75%](#item-26) ⭐️ 6.0/10
27. [Local Web Tool Plans City Radio Mesh Networks](#item-27) ⭐️ 6.0/10
28. [GhostScript Upload2Shell Vulnerability Draws Security Attention](#item-28) ⭐️ 6.0/10
29. [OpenAI Scientist Proposes Measuring AI Development Speed](#item-29) ⭐️ 6.0/10
30. [Nvidia’s Earnings Contrast With Pressure for Huang’s Return](#item-30) ⭐️ 6.0/10
31. [AI Face Licensing Tests Hollywood’s Future](#item-31) ⭐️ 6.0/10
32. [GLP-1 Drugs Could Free Farmland Larger Than Italy](#item-32) ⭐️ 6.0/10
33. [Meta Reconsiders 2030 Net-Zero Goal as AI Emissions Rise](#item-33) ⭐️ 6.0/10
34. [Isaac Developer Removes AI Music After Backlash](#item-34) ⭐️ 6.0/10
35. [Sterilized Soil Kept Lifelike Reactions Alive for Six Years](#item-35) ⭐️ 6.0/10
36. [Super El Niño Could Intensify Global Hunger](#item-36) ⭐️ 6.0/10
37. [AI Accelerates the Race to Patch Vulnerabilities](#item-37) ⭐️ 6.0/10
38. [OpenAgentCore Brings a Self-Hosted OpenAI Agents API](#item-38) ⭐️ 6.0/10
39. [Three Controls for Recovery JWTs and JWKS Rotation](#item-39) ⭐️ 6.0/10
40. [Role-Separated AI Agents for Safer Pull Request Review](#item-40) ⭐️ 6.0/10
41. [Inventory PDF.js Viewers by Origin, Not Product Name](#item-41) ⭐️ 6.0/10
42. [Assisted Reproduction Amid Declining Fertility Rates](#item-42) ⭐️ 6.0/10
43. [Health Professionals Urged to Support Detained Palestinian Colleagues](#item-43) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Perplexity as a Signal of Model Intelligence](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 8.0/10

OpenAI Chief Scientist Jakub Pachocki argues that pretraining perplexity may be a simple, consistently useful indicator of a model’s general learned intelligence. The article also examines where perplexity diverges from actionable task evaluations and from gains produced by post-training methods such as reinforcement learning. If improvements in perplexity reliably precede gains in broader capabilities, the metric could offer researchers a more informative tracking signal than proliferating isolated benchmarks. However, post-training reasoning methods can create major performance discontinuities, so perplexity alone should not be treated as a complete measure of frontier-model capability. Perplexity is the exponentiated average negative log-likelihood of held-out tokens, expressing how surprising a model finds the data; an ideal deterministic predictor approaches 1, while uniform random guessing over a vocabulary V approaches V. The article distinguishes perplexity’s apparent link to general intelligence from direct task relevance and from advances occurring outside pretraining, while commenters question whether abilities truly emerge at fixed perplexity thresholds.

hackernews · Hacker News \(热门\) · Nov 22, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50601525)

**Background**: Perplexity measures how accurately a language model predicts tokens, and it has long been optimized during pretraining because lower loss generally indicates a better probabilistic model of text. The article proposes treating perplexity as a possible proxy for general learned intelligence rather than merely a training loss. Chain-of-thought training and reinforcement learning can improve reasoning after pretraining, making the relationship between lower perplexity and frontier performance an open question.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/perplexity-and-intelligence/">Perplexity and Intelligence | OpenAI</a></li>
<li><a href="https://canvas4everyone.com/blogs/news/unraveling-the-relationship-between-perplexity-and-kullback-leibler-divergence">Unraveling the Relationship Between Perplexity and Kullback-Leibler Di</a></li>
<li><a href="https://liner.com/review/paloma-benchmark-for-evaluating-language-model-fit">Paloma: A Benchmark for Evaluating Language Model Fit...</a></li>

</ul>
</details>

**Discussion**: Participants found the apparent perplexity trend striking and welcomed a simple benchmark, while one commenter supplied a technical definition of perplexity. Others highlighted GPT-4.5 as a possible discontinuity, suggesting that chain-of-thought and reinforcement learning produced stronger real-world gains than perplexity alone captures, and questioned whether specialized models can display high task performance despite relatively weak general perplexity.

**Tags**: `#language-models`, `#perplexity`, `#pretraining`, `#reinforcement-learning`, `#model-evaluation`

---

<a id="item-2"></a>
## [Anthropic’s 2028 Power Mix Is Mostly Gas and Coal](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/) ⭐️ 8.0/10

A Better Data Center Project case study projects that Anthropic’s contracted U.S. data centers could obtain about 87% of their electricity from natural gas and 11% from coal in 2028. The estimate, based on permits, regulatory filings, and EPA modeling rather than a measured operating mix or an Anthropic statement, also indicates potential annual emissions of 17 to 38 million metric tons of CO2 equivalent under the mid-case scenario. The projection highlights how the rapid expansion of AI computing may be tied to fossil-fuel generation rather than renewable energy, creating substantial carbon, air-pollution, water-use, and grid-planning challenges. It also strengthens pressure on regulators, policymakers, and customers to address infrastructure costs and environmental effects that local communities may otherwise bear. The analysis covers about 15 gigawatts of contracted Anthropic compute and links its projected power mix to data centers, associated power plants, and on-site gas turbines. These figures are forward-looking estimates tied to 2028 infrastructure plans, so they should not be treated as Anthropic’s current electricity mix or proof that every projected facility will operate as assumed.

hackernews · Hacker News \(热门\) · Nov 22, 08:57 · [Discussion](https://news.ycombinator.com/item?id=50597612)

**Background**: The case study examines a model commonly described as “bring your own power,” in which large data-center operators arrange dedicated generation and grid connections to meet rapidly rising computing demand. AI infrastructure generally requires substantial electricity, water, land, and cooling infrastructure, while its operational emissions depend heavily on the local generation mix. Researchers have called for AI expansion to be integrated into energy, water, and land-use planning to reduce resource pressure and environmental harm.

<details><summary>References</summary>
<ul>
<li><a href="https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/">How AI is powered : a breakdown of BYOP and grid power</a></li>
<li><a href="https://explainx.ai/blog/anthropic-data-center-power-gas-coal-byop-2028-better-datacenter-november-2026">Anthropic Power Mix: 87% Gas, 11% Coal by 2028 (Study ...</a></li>
<li><a href="https://news.un.org/en/story/2026/06/1167658">AI’s environmental costs threaten water, land and climate ...</a></li>

</ul>
</details>

**Discussion**: Commenters broadly condemned Anthropic’s environmental record and contrasted it with stronger renewable-energy commitments by other technology companies. They argued for regulation that accounts for social and environmental externalities, expressed concern about pollution around facilities such as Colossus 1 in Memphis, and noted that abundant U.S. shale gas may often be a byproduct of oil production, complicating claims that switching to gas would decouple AI growth from fossil fuels.

**Tags**: `#AI infrastructure`, `#data-center energy`, `#natural gas`, `#climate policy`, `#environmental impact`

---

<a id="item-3"></a>
## [Inkling-2-Mini Runs in 5.4 GB at 150 Tokens per Second](https://github.com/ShinMegamiBoson/lookatmyquant) ⭐️ 8.0/10

The lookatmyquant project demonstrates a heavily quantized Inkling-2-Mini deployment that fits within a reported 5.4 GB memory footprint. Custom GPU kernel work enables roughly 150 tokens per second on two NVIDIA RTX A4500 GPUs linked with NVLink. This deployment illustrates how low-bit quantization and specialized kernels can make a 26.4B-parameter open-weight model practical on comparatively modest local hardware. It also highlights the continuing narrowing of the capability gap between frontier models and locally run open models, although the result depends on custom engineering. Inkling-2-Mini is a 26.4B Mixture-of-Experts model with 5.4B active parameters, using a looped-transformer architecture designed for coding, agentic, and vision workloads. The reported 5.4 GB figure should not be confused with total system requirements: other users report needing substantially more VRAM for practical context lengths, particularly with a 128K KV cache, and measured speed varies sharply by GPU and kernel implementation.

hackernews · Hacker News \(热门\) · Nov 21, 18:02 · [Discussion](https://news.ycombinator.com/item?id=50591853)

**Background**: Quantization stores model weights at reduced numerical precision, lowering memory consumption and often accelerating inference at the cost of potential output-quality changes. Inkling-2-Mini uses a looped-transformer design and sparse MoE activation, allowing only 5.4B of its 26.4B parameters to participate in each token computation. Low-bit formats such as NVFP4 can reduce storage further, but efficient execution generally requires carefully optimized GPU kernels.

<details><summary>References</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Introducing Inkling 2 Mini - Thinking Machines Lab</a></li>
<li><a href="https://unsloth.ai/docs/models/inkling-2-mini">Inkling 2 Mini - Run Locally Guide | Unsloth Documentation</a></li>
<li><a href="https://www.techpowerup.com/gpu-specs/rtx-a4500.c3849">NVIDIA RTX A 4500 Specs | TechPowerUp GPU Database</a></li>

</ul>
</details>

**Discussion**: Community members consider Inkling-2-Mini capable and reported successful coding and Grafana tasks, but warned that running a model is not the same as obtaining useful quality. Performance reports diverge widely, with one user measuring only one-third the speed of Qwen 27B on an R9700 and another saying credible 100K-plus context performance required at least 12 GB of VRAM; users also questioned benchmark claims and the repository&\#x27;s documentation.

**Tags**: `#quantization`, `#local-llm`, `#model-inference`, `#GPU-kernels`, `#edge-ai`

---

<a id="item-4"></a>
## [OpenRouter Removes Providers After Prompt Privacy Incidents](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) ⭐️ 8.0/10

OpenRouter said it investigated incidents in which inference providers improperly retained or accessed prompts, including routing through an upstream provider rather than processing requests as expected. It removed three providers, stripped 125 endpoints of Zero Data Retention eligibility, notified potentially affected customers, and outlined interim privacy, routing, and ZDR safeguards. The incidents show that a gateway&\#x27;s privacy claims can depend on how each downstream provider handles requests, especially when providers are silently rerouted to other backends. Organizations using OpenRouter may therefore need provider allowlists, direct contracts, contractual ZDR terms, and independent assurance rather than relying on a platform-wide designation. 受影响的范围包括研究人员发现的服务商，以及作为预防措施额外移除的端点。零数据保留通常意味着推理完成后不存储提示词和响应，但其适用范围、例外情况和执行方式会因服务商而异，因此应按端点核验资格，不能把所有端点视为具有同等的隐私保障。

hackernews · Hacker News \(热门\) · Nov 22, 02:14 · [Discussion](https://news.ycombinator.com/item?id=50595554)

**Background**: OpenRouter is a unified API gateway that routes model requests among third-party inference providers. ZDR is intended to prevent an inference provider from retaining prompts and outputs after processing, but disclosures can reveal discrepancies between a provider&\#x27;s advertised endpoint identity and the infrastructure that ultimately handles the request.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/">Data Processing Incidents on Inference Providers</a></li>
<li><a href="https://openrouter.ai/blog/insights/zero-data-retention/">Zero Data Retention (ZDR): What It Means for AI APIs</a></li>
<li><a href="https://www.spheron.network/blog/zero-data-retention-for-llm-inference-what-a-fixed-plan-guar/">Zero Data Retention for LLM Inference: What a Fixed Plan ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong concern that OpenRouter lacked adequate provider due diligence and that its initial safeguards lacked the force of direct contractual protections. Some welcomed the response but stressed that the strongest ZDR agreement is one negotiated directly with the inference provider; smaller organizations said they may lack the scale or budget for that and favored allowlisting trusted providers, while one affected user reported only one nonsensitive prompt being involved.

**Tags**: `#AI privacy`, `#inference providers`, `#OpenRouter`, `#prompt security`, `#data retention`

---

<a id="item-5"></a>
## [Japanese Automakers Standardize Parts to Cut Costs](https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/) ⭐️ 7.0/10

Toyota, Nissan, Honda, and four other Japanese automakers are pursuing parts commonization to simplify production and reduce costs. The effort is particularly aimed at improving their competitiveness against lower-cost Chinese automakers. Shared components could lower development, procurement, and manufacturing expenses across a broader range of vehicles, potentially influencing vehicle prices and industry-wide manufacturing practices. The strategy may also help Japan’s seven automakers respond to strong Chinese competition and, for Nissan, ease financial pressure. Parts commonization means deliberately using the same parts, modules, interfaces, or engineering specifications across vehicles, trims, platforms, plants, or regions. Its savings depend on meaningful component volume and careful engineering, and the initiative also requires coordination among Toyota, Nissan, Honda, Mazda, Subaru, Mitsubishi, and Suzuki.

hackernews · Hacker News \(热门\) · Nov 22, 04:04 · [Discussion](https://news.ycombinator.com/item?id=50596133)

**Background**: Automakers have long reduced costs through platform engineering, in which different vehicles share underlying structures and components. Such reuse can simplify development and production, but it has technical limits and requires compatible designs without compromising vehicle quality or performance. Chinese manufacturers have increased pressure on Japanese automakers by competing with aggressive pricing and, in some cases, extensive in-house component production.

<details><summary>References</summary>
<ul>
<li><a href="https://umbrex.com/resources/umbrex-explainers/automotive-mobility-explainers/parts-commonization/">What is parts commonization? | Umbrex Explainers</a></li>
<li><a href="https://resources.hartfordtechnologies.com/blog/future-standardization-of-methods-and-cost-structures-in-automotive-manufacturing">Future Standardization of Methods and Cost Structures in ...</a></li>
<li><a href="https://www.arabakirala.com.tr/en/blog/automotive-parts-standardization-shared-components">Automotive Parts Standardization and Shared Components</a></li>

</ul>
</details>

**Discussion**: Commenters viewed parts commonization as a sensible response to Chinese cost competition, with one comparison to GM and Ford’s shared six-speed automatic transmission program dating to 2002. They also highlighted Chinese firms’ high levels of vertical integration, questioned whether the headline understated the industry-wide scope, and suggested the effort may provide relief for Nissan amid its financial troubles. One commenter questioned affordability for unemployed consumers, while some posted material was truncated.

**Tags**: `#automotive-industry`, `#manufacturing`, `#supply-chain`, `#electric-vehicles`, `#cost-reduction`

---

<a id="item-6"></a>
## [Show HN: A Game Where You Are an LLM Subagent](https://github.com/gulivan/worker755) ⭐️ 7.0/10

Show HN featured worker755, an open-source game in which players issue tasks to an LLM manager and interact with the subagents to whom it delegates work. The project received 230 points and 56 comments on Hacker News. The project turns hierarchical agent delegation into an interactive and entertaining experience, demonstrating how LLM orchestration can be presented to users rather than merely discussed as an enterprise architecture pattern. It is best understood as an engaging demonstration rather than a major technical advance. The game supports experimenting with destructive commands such as attempting to remove every file, while the manager&\#x27;s behavior determines how much guidance players receive. A noted limitation is the apparent absence of local LLM support, which prevents use with a self-hosted homelab server.

hackernews · Hacker News \(热门\) · Nov 22, 13:56 · [Discussion](https://news.ycombinator.com/item?id=50599762)

**Background**: In multi-agent systems, an orchestrator or manager agent can divide a larger objective into subtasks and assign them to specialized subagents. This worker755 game makes that delegation model playable: the player acts as a subagent while an LLM manager coordinates tasks and responds to requests.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/agents/architecture/multi-agent-orchestrator-sub-agent">Orchestrator and subagent multi-agent patterns | Microsoft Learn</a></li>
<li><a href="https://martinuke0.github.io/posts/subagents/">Sub-Agents in LLM Systems : Architecture, Execution Model ...</a></li>
<li><a href="https://arxiv.org/html/2601.13671v1">The Orchestration of Multi-Agent Systems: Architectures ...</a></li>

</ul>
</details>

**Discussion**: Players generally found the game fun and praised its creative treatment of agent delegation. Some wanted the manager to stop revealing exact commands and allow more independent play, while another commenter wanted local LLM support; playful suggestions also included trying to delete every file and deploying reverse Turing tests against humans.

**Tags**: `#LLM agents`, `#AI games`, `#multi-agent systems`, `#developer tools`, `#open source`

---

<a id="item-7"></a>
## [Alliance Proposes Open Protocol for Social Media](https://osw-alliance.net/en/) ⭐️ 7.0/10

The Open Social Web Alliance is advocating a shared, standardized communication protocol for interoperable and resilient social media. Its policy paper proposes decentralized social infrastructure and sets a goal of reaching 100 million users on open social networks by 2028. A common open protocol could reduce dependence on closed platforms and make services easier to migrate between, potentially improving user control and resilience. The proposal also seeks to strengthen democratic discourse, although its economic and governance assumptions remain open to debate. The alliance identifies infrastructure, governance, funding, appeal, and public mandate as five central challenges. The supplied homepage offers little technical detail, so the proposal&\#x27;s exact protocol design, implementation readiness, and funding model are not yet clear from the available material.

hackernews · Hacker News \(热门\) · Nov 22, 15:24 · [Discussion](https://news.ycombinator.com/item?id=50600511)

**Background**: An open social protocol is a shared technical standard that allows people and services built by different organizations to communicate and exchange social content. Existing examples include ActivityPub, a W3C-recommended decentralized networking standard, and the AT Protocol and Nostr, both designed around open or decentralized social-network approaches. Such protocols seek to avoid lock-in by separating the underlying communication layer from individual applications and service providers.

<details><summary>References</summary>
<ul>
<li><a href="https://osw-alliance.net/en/">Open Social Web Alliance – OSW-Alliance.net</a></li>
<li><a href="https://eu.boell.org/sites/default/files/2026-10/oswa_policypaper_en_digital.pdf">Open Social Web Alliance</a></li>
<li><a href="https://www.w3.org/TR/activitypub/">ActivityPub - World Wide Web Consortium (W3C)</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the goal of trustworthy, bot-resistant, non-retention-maximizing alternatives but criticized the alliance&\#x27;s prose as vague and technically uninformative. They also questioned whether democracy can be engineered through software, arguing that anger and discord are often easier to monetize than constructive participation; one commenter also warned that users are unlikely to migrate en masse unless the new system offers compelling practical benefits.

**Tags**: `#open social web`, `#protocols`, `#social media`, `#interoperability`, `#online democracy`

---

<a id="item-8"></a>
## [Delta Flights Delayed After Atlanta Weight-and-Balance System Outage](https://www.nytimes.com/2026/11/22/us/delta-flight-delays-system-outage.html) ⭐️ 7.0/10

An outage in Delta Air Lines&\#x27; automated weight-and-balance system disrupted flights at Atlanta and other hubs, with reports citing delays to at least 3,500 flights. Staff had to count bags and calculate aircraft weight manually while the FAA briefly imposed a ground stop on Atlanta-bound flights. The incident shows how a failure in a single operational calculation system can cascade into widespread delays across a carrier&\#x27;s network. It also highlights the risks of relying on tightly integrated automation during periods of exceptionally heavy holiday travel. The failed system automates aircraft weight-and-balance calculations, a safety-critical process used to determine whether departing aircraft are properly loaded. Reports say staff fell back to manual baggage counting and weight calculations; the cause of the outage and the full scope of affected flights were not established in the available results.

rss · Hacker News \(热门\) · Nov 22, 19:51

**Background**: Hartsfield–Jackson Atlanta International Airport is Delta&\#x27;s largest hub, so operational disruption there can affect many connecting itineraries as well as other Delta hubs. Aircraft weight-and-balance systems calculate load limits and distribute weight for safe flight; airline operations control centers coordinate flight dispatch, aircraft status, crew scheduling, maintenance, weather, air traffic services, and customer support. A manual workaround can preserve safety but is slower and harder to scale, particularly during peak travel periods.

<details><summary>References</summary>
<ul>
<li><a href="https://www.foxnews.com/us/faa-lifts-ground-stop-atlanta-bound-delta-flights-system-outage">Delta weight and balance outage reportedly delays 3,500 flights at hubs</a></li>
<li><a href="https://www.zerohedge.com/markets/deltas-biggest-hub-hit-automation-issue-sparking-delays-thanksgiving-travel-ramps">Delta &#x27;s Biggest Hub Hit By &quot; Automation Issue,&quot; Sparking... | Zero...</a></li>
<li><a href="https://www.flightatom.com/resources/airline-operations-control-centre.html">OCC in Aviation: What an Operations Control Centre Does</a></li>

</ul>
</details>

**Tags**: `#airline-operations`, `#system-outage`, `#infrastructure-resilience`, `#automation`, `#incident-response`

---

<a id="item-9"></a>
## [Muru Brings Rust-Powered Python Serving to ASGI and WSGI](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

Graham Dumpleton, creator of mod\_wsgi, introduced Muru, an AI-assisted Rust application server for running both ASGI and WSGI Python applications in development and production. He is documenting the project through a detailed series of posts covering worker architecture, zero-downtime releases, Kubernetes integration, autoscaling, tracing, and other design choices. Muru could give Python teams a modern server architecture that supports synchronous and asynchronous applications while reducing the operational complexity associated with production deployment. Its creator&\#x27;s two decades of experience with mod\_wsgi and its explicit integration with containers and Kubernetes may make it particularly relevant to teams seeking a unified development-to-production platform. Muru&\#x27;s design includes importing the application once and forking workers, supporting WSGI and ASGI together, performing releases without full server restarts, using canaries without a service mesh, and working with Kubernetes rather than around it. Dumpleton says AI performs much of the surface-level work, while he retains responsibility for evaluating adequacy and continuing to refine the server until he would trust it in production.

rss · Simon Willison \(AI 跨行业洞察\) · Nov 21, 23:56

**Background**: WSGI is Python&\#x27;s standard interface for synchronous web applications, while ASGI supports asynchronous applications and protocols such as WebSockets, including compatibility paths for synchronous applications. mod\_wsgi is a long-established Apache module for hosting WSGI applications in production and is maintained by Muru creator Graham Dumpleton. Muru is intended as a new standalone server that combines modern deployment capabilities with support for both interfaces.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/python/difference-between-asgi-and-wsgi-in-django/">Difference Between ASGI and WSGI in Django - GeeksforGeeks</a></li>
<li><a href="https://asgi.readthedocs.io/en/latest/">ASGI Documentation — ASGI 3.0 documentation</a></li>
<li><a href="https://modwsgi.readthedocs.io/en/master/">mod_wsgi — mod_wsgi 6.1.1 documentation</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Rust`, `#ASGI`, `#WSGI`, `#Application Servers`

---

<a id="item-10"></a>
## [Two Million AI Canary Tokens Expose Supply-Chain Privacy Failures](https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/) ⭐️ 7.0/10

A security researcher seeded two million unique canary tokens into AI prompts across the supply chain, then traced where they appeared. The tests uncovered three provider breaches, prompt theft, and cases in which Zero Data Retention settings were ignored. The findings show that sensitive information submitted to AI services may persist, travel through downstream infrastructure, or appear in places operators believe are private. This creates material privacy and security risks for users whose prompts contain credentials, proprietary data, or personal information. Each secret was previously unused, and the researcher controlled the infrastructure receiving requests, allowing every token to be linked to exactly one prompt sent to one provider. A canary token is a unique, trackable string embedded as a tripwire for detecting unauthorized disclosure or context leakage.

rss · Lobsters \(技术社区\) · Nov 22, 02:03

**Background**: AI supply chains can involve model providers, application platforms, logging systems, and downstream processors that handle prompts or generated outputs. Canary tokens make otherwise invisible leakage measurable by revealing where planted data later appears. Zero Data Retention settings are intended to prevent service providers from storing submitted data, but the reported tests found some providers disregarding them.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens">AI Supply Chain Security: What Canary Tokens Found | Dragos ...</a></li>
<li><a href="https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/">Researcher plants 2m canaries into the AI supply chain . - Ars Technica</a></li>
<li><a href="https://inferensys.com/glossary/agentic-threat-modeling/agent-output-validation/canary-token">Canary Token: Definition, Detection &amp; Security | Inference ...</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#supply-chain security`, `#data privacy`, `#secret leakage`, `#canary tokens`

---

<a id="item-11"></a>
## [Packaging PostgreSQL as a Single Binary](https://progrium.xyz/articles/2026/single-binary-postgres) ⭐️ 7.0/10

The article presents an engineering approach for packaging PostgreSQL and its required components into one executable file. The linked summary also suggests that the method may be reusable for packaging other complex systems for specialized deployment scenarios. A self-contained PostgreSQL binary could simplify distribution, testing, and deployment in environments where package managers or containers are inconvenient. The approach may also establish a reusable model for turning other multi-component systems into portable applications. The provided material does not disclose the article&\#x27;s implementation steps, supported platforms, PostgreSQL version, extension-loading behavior, or build-system tradeoffs. PostgreSQL normally relies on separately packaged components and dynamically loadable modules, so a complete single-binary implementation must address those runtime dependencies and compatibility constraints.

rss · Lobsters \(技术社区\) · Nov 21, 19:32

**Background**: PostgreSQL is available through operating-system packages and installers, while building it from source is primarily recommended for development and extension work. Packaging it as one executable would bundle the database server and associated runtime assets, reducing setup friction for portable, embedded, or tightly controlled deployments.

<details><summary>References</summary>
<ul>
<li><a href="https://progrium.xyz/articles/2026/single-binary-postgres">How I Got Postgres into a Single Binary · progrium</a></li>
<li><a href="https://www.postgresql.org/docs/current/install-binaries.html">PostgreSQL: Documentation: 18: Chapter 16. Installation from ...</a></li>
<li><a href="https://www.postgresql.org/docs/current/xfunc-c.html">PostgreSQL : Documentation: 19: 36.10. C-Language Functions</a></li>

</ul>
</details>

**Tags**: `#PostgreSQL`, `#Single Binary`, `#Software Packaging`, `#Deployment`, `#Systems Engineering`

---

<a id="item-12"></a>
## [Microsoft 365 Outage Post-Incident Report Explains Root Cause](https://tianyin.github.io/misc/pir_microsoft_365_11-12-2026.pdf) ⭐️ 7.0/10

Microsoft published a post-incident report examining a widespread Microsoft 365 outage that disrupted services including Outlook, Teams, and Copilot. The report describes recovery measures such as restoring stable connection-handling code, clearing delayed emails, expanding server capacity, and adding protections against cascading failures. The report offers concrete lessons for service reliability, incident response, and infrastructure resilience in a platform used by organizations worldwide. It also illustrates how a defect in a shared connection-handling component can affect many otherwise independent Microsoft 365 services. Available reporting attributes the outage to a months-old Windows bug that impaired more than 80% of servers, while Microsoft says it restored the stable connection-handling implementation and added defense-in-depth safeguards. The material supplied here is only a link to discussion comments, so the full report&\#x27;s technical depth and the quality of community discussion cannot be independently assessed from the provided content.

rss · Lobsters \(技术社区\) · Nov 21, 12:22

**Background**: A post-incident report, also called a postmortem, documents what failed during a service outage, why it happened, how the incident was mitigated, and what changes are planned to reduce recurrence risk. Microsoft 365 is a collection of hosted productivity services, so a failure in shared infrastructure can interrupt several applications at once and generate delayed messages or connection errors during recovery.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/microsoft-reveals-root-cause-of-massive-microsoft-365-outage-as-months-old-windows-bug-crippled-over-80-of-servers/">Microsoft Reveals Root Cause Of Massive Microsoft 365 Outage , As...</a></li>
<li><a href="https://ppc.land/microsoft-365-email-outage-hits-19-services-from-outlook-to-copilot/">Microsoft 365 email outage hits 19 services , from Outlook to Copilot</a></li>
<li><a href="https://www.bleepingcomputer.com/news/microsoft/massive-microsoft-365-outage-disrupts-outlook-teams-copilot-worldwide/">Massive Microsoft 365 outage disrupts Outlook, Teams, Copilot...</a></li>

</ul>
</details>

**Tags**: `#Microsoft 365`, `#service reliability`, `#incident response`, `#postmortem`, `#infrastructure`

---

<a id="item-13"></a>
## [Signal Restricts Mobile Screenshots Over AI Surveillance Concerns](https://techcrunch.com/2026/11/21/signal-restricts-mobile-screenshots-as-it-confronts-existential-threat-of-ai-surveillance/) ⭐️ 7.0/10

Signal is limiting users’ ability to take screenshots in both its Android and iOS applications. The change extends protections it had already applied by default to the Windows app in response to the risk that AI assistants could analyze captured conversations. The restriction is intended to preserve Signal’s privacy guarantees as device makers integrate AI assistants capable of interpreting on-screen content. It affects a widely used encrypted messaging service and highlights growing tension between mobile convenience, system-level AI, and protection against unwanted surveillance. Android can enforce strong screenshot and display-capture blocking through the FLAG\_SECURE window flag, whereas iOS lacks an equivalent universal prevention mechanism and generally relies on detection signals such as screenshot notifications. Signal’s users can disable the new restriction, although Signal’s president Meredith Whittaker reportedly said doing so would break the service’s privacy guarantees.

rss · TechCrunch AI · Nov 21, 21:37

**Background**: Signal is an encrypted messaging application, but encrypted transmission does not by itself prevent a user or an operating-system feature from capturing information already displayed on a screen. The reported concern is that built-in AI assistants such as Apple’s Siri AI and Google Gemini could read private chats through screen capture. Android and iOS offer different technical controls for resisting or detecting screenshots and recordings.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/21/signal-restricts-mobile-screenshots-as-it-confronts-existential-threat-of-ai-surveillance/">Signal restricts mobile screenshots as it confronts ...</a></li>
<li><a href="https://screenshotneo.com/blog/detect-screenshots-android-api/">How to Detect Screenshots on Android with an API · ScreenshotNeo</a></li>
<li><a href="https://stackoverflow.com/questions/77151044/how-to-prevent-user-from-taking-screenshot-or-screen-recording-in-ios-17">swift - How to prevent user from taking screenshot or... - Stack Overflow</a></li>

</ul>
</details>

**Tags**: `#Signal`, `#Mobile Security`, `#AI Surveillance`, `#Privacy`, `#Screenshot Prevention`

---

<a id="item-14"></a>
## [Race Realism Fails Modern Genetics](https://arstechnica.com/science/2026/11/race-realism-isnt-realistic-and-it-isnt-good-science/) ⭐️ 7.0/10

The article argues that biologically innate racial differences in intelligence are neither realistic nor scientifically valid under modern genetics. It criticizes “race realism” as a claim that contemporary population-genetic evidence cannot substantiate. Claims linking immutable racial categories to inherited intelligence can misattribute differences shaped by environment to biology and influence education, policy, and public debate. The critique matters because it shifts attention toward how population variation, genetic ancestry, and environmental conditions interact rather than treating race as a straightforward biological cause. Human genetic diversity is often described through clines, in which genetic or phenotypic frequencies change gradually across geography, rather than discrete biological races. Intelligence is heritable within populations, but heritability does not by itself establish innate differences between racial groups or identify the causes of differences between populations, where environmental effects and population history must also be considered.

rss · Ars Technica · Nov 21, 12:01

**Background**: In population genetics, a cline is a gradual geographic change in allele or phenotype frequencies; interbreeding populations can therefore show continuous variation rather than sharply bounded subspecies. The “Lewontin fallacy” debate concerns the mistaken inference from substantial genetic variation within populations to the absence of meaningful variation between them. Separately, twin studies estimate how much variation in intelligence is attributable to genetic differences, but that estimate does not determine which groups differ, why they differ, or whether racial labels identify coherent biological populations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bionity.com/en/encyclopedia/Cline_%28population_genetics%29.html">Cline _( population _ genetics )</a></li>
<li><a href="https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2016.00022/full">Frontiers | Population Genomics and the Statistical Values of Race ...</a></li>
<li><a href="https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01622/full">Frontiers | Genetics and Learning: How the Genes Influence...</a></li>

</ul>
</details>

**Tags**: `#genetics`, `#race`, `#intelligence`, `#scientific-method`, `#population-biology`

---

<a id="item-15"></a>
## [FCC Blocks California’s AT&amp;T Home Phone Rules](https://arstechnica.com/tech-policy/2026/11/fcc-orders-california-to-stop-enforcing-phone-service-rules-against-att/) ⭐️ 7.0/10

The FCC has preempted California rules that would require AT&amp;T to continue offering traditional home phone service. The order limits California’s authority to compel AT&amp;T to maintain that service. The decision represents federal preemption of state telecommunications regulation and could affect how other states protect consumers from the retirement of copper-based landlines. It also gives AT&amp;T and other providers greater flexibility as fixed voice service migrates toward cable, mobile, and VoIP alternatives. FCC rules generally require providers to offer affected customers an adequate replacement before discontinuing copper voice service, including cable phone service or 4G or 5G mobile service. The brief report does not provide the full order, legal reasoning, implementation timeline, or the precise scope of California’s displaced rules.

rss · Ars Technica · Nov 20, 22:28

**Background**: The FCC can preempt conflicting state and local telecommunications laws under federal authority. Traditional home phone service has increasingly shifted from copper networks toward cable-based service, mobile service, and VoIP, requiring regulators to balance provider flexibility with consumer protections during the transition.

<details><summary>References</summary>
<ul>
<li><a href="https://www.congress.gov/crs_external_products/R/PDF/R46736/R46736.6.pdf">Stepping In: The FCC s Authority to Preempt State Laws Under ...</a></li>
<li><a href="https://www.fcc.gov/tech-transitions">Tech Transition: Modernizing Communications Services</a></li>
<li><a href="https://www.fcc.gov/consumers/guides/consumer-protections-home-phone-services">Consumer Protections for Home Phone Service | Federal ...</a></li>

</ul>
</details>

**Tags**: `#FCC`, `#telecommunications policy`, `#California`, `#AT&amp;T`, `#federal preemption`

---

<a id="item-16"></a>
## [Banks Restrict Third-Party AI Agents and Shift Liability](https://www.wired.com/story/banks-are-cracking-down-on-ai-agents/) ⭐️ 7.0/10

Major US banks are blocking or restricting third-party AI agents that log into customer accounts, particularly when agents use customer credentials directly. They are also warning customers that losses caused by unauthorized or mistaken agent actions may remain the customer&\#x27;s responsibility. The measures make credential-based consumer AI agents harder to deploy and place responsibility for agent errors with customers unless the bank&\#x27;s own systems or authorized tools are involved. This could reshape agentic AI in banking toward bank-controlled platforms, read-only access, and stronger auditability. JPMorgan, Bank of America, and Citi are restricting agent access, while many banks are moving toward read-only connections through authorized data connectors. Morgan Stanley has begun blocking third-party agents from its platforms; reports also describe some agents taking actions that appeared independent of customers&\#x27; instructions.

rss · Wired · Nov 22, 11:00

**Background**: Third-party AI agents can automate financial tasks by acting on a customer&\#x27;s behalf, but some authenticate using the customer&\#x27;s own banking username and password rather than an institution-approved connection. Authorized data connectors and bank-operated agent platforms offer more controlled alternatives by applying policies, approvals, and audit trails within the bank&\#x27;s systems.

<details><summary>References</summary>
<ul>
<li><a href="https://news.slashdot.org/story/26/10/23/0023257/unvetted-ai-agents-are-accessing-us-bank-accounts">Unvetted AI Agents Are Accessing US Bank Accounts - Slashdot</a></li>
<li><a href="https://pwn.watch/i/us-banks-unauthorized-ai-agents-customer-accounts">Major U.S. banks detect unauthorized third - party AI agents inside...</a></li>
<li><a href="https://aistocktradingbots.com/blog/banks-block-ai-agents-customer-logins/">Morgan Stanley, JPMorgan and Citi Block AI Agents That Use...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#financial security`, `#banking`, `#access control`, `#liability`

---

<a id="item-17"></a>
## [Telltale Reads Back QNX 8.0 Instrument Pixels to Catch False Displays](https://dev.to/edycutjong/a-heartbeat-cant-tell-you-the-speedometer-is-lying-reading-the-glass-back-on-qnx-80-1gbd) ⭐️ 7.0/10

The open-source Telltale watchdog runs as a separate QNX 8.0 process, reads pixels composed by QNX Screen, decodes the speedometer digits, six warning lamps, and a liveness tick, and compares the rendered output with vehicle state. In a recorded QEMU test, it detected a frozen speedometer 123.4 ms after the fault and placed a verified safe display on screen at 181.3 ms. A healthy renderer process, an advancing heartbeat, or a correct internal report does not prove that a driver is seeing correct information. Pixel-level readback offers a practical end-to-end check for automotive instrument clusters, especially where stale, blank, or misdrawn values could mislead drivers. The test replayed a deceleration from 49.01 km/h to zero in 4.848 seconds using the comma2k19 dataset and injected a renderer freeze. Telltale caught all 50 STALE runs, all 50 BLANK runs, and all 10 MISDRAW runs through deterministic glyph decoding; its results were measured under QEMU with TCG on an x86\_64 QNX 8.0 guest, not on hardware, and the tool is not certified or ISO 26262 or ASIL compliant.

rss · Dev.to · Nov 22, 21:24

**Background**: QNX Screen composes graphics for embedded and automotive displays, while QNX 8.0 provides the operating-system environment in which the instrument-cluster renderer runs. Conventional watchdogs often verify process liveness, but they may miss a renderer that remains alive yet presents an obsolete or incorrect speedometer value. Telltale instead applies an end-to-end assertion to the final pixels visible to the driver, using a known glyph atlas rather than machine learning.

<details><summary>References</summary>
<ul>
<li><a href="https://www.qnx.com/developers/docs/8.0/com.qnx.doc.neutrino.lib_ref/topic/full_safety.html">Full Safety Information - qnx.com</a></li>
<li><a href="https://qnx.software/en/software/products-and-solutions/qnx-os-and-os-for-safety">QNX OS and OS for Safety</a></li>

</ul>
</details>

**Tags**: `#QNX 8.0`, `#automotive software`, `#display testing`, `#pixel readback`, `#safety-critical systems`

---

<a id="item-18"></a>
## [Answer Receipts Make Text-to-SQL Results Auditable](https://dev.to/prachitparikh/text-to-sql-answer-receipts-the-spec-id-write-before-an-ai-agent-answers-one-data-question-1jm2) ⭐️ 7.0/10

The article proposes that text-to-SQL agents return structured answer receipts alongside every metric, documenting metric definitions, interpretations, defaults, filters, time boundaries, source queries, and provenance. It also gives business analysts requirements for deciding when material ambiguity should trigger a clarification question rather than an unqualified answer. The proposal addresses a common enterprise AI failure mode: technically valid SQL can still answer a different business question from the one intended. Auditable receipts and explicit clarification thresholds could reduce incorrect dashboards and executive decisions while making AI-generated analytics resemble governed, human-reviewed reporting. The illustrated fixture contains five plausible readings of “revenue last month” that produce values from $5,550 to $8,550, a 54% spread despite correct execution on a ten-row table. The proposed receipt records definition identifiers, grain, filters, time range, timezone, unstated defaults, SQL, and row counts at key stages; agents should generate and test multiple interpretations, then ask a question when their results diverge materially.

rss · Dev.to · Nov 22, 21:22

**Background**: Text-to-SQL systems translate natural-language requests into database queries, but successful execution does not guarantee that the business metric matches the user’s intent. A semantic layer addresses this by centralizing business logic, metric definitions, hierarchies, and calculations across analytics tools. Agent observability frameworks such as Langfuse, MLflow, and Pydantic Logfire provide a related foundation by tracing model calls, database queries, inputs, outputs, and intermediate metadata.

<details><summary>References</summary>
<ul>
<li><a href="https://omni.co/articles/best-semantic-layer-for-ai-and-bi-2026">Semantic Layer for AI and BI (2026): Why It Matters... - Omni Analytics</a></li>
<li><a href="https://www.dremio.com/resources/guides/what-is-a-semantic-layer/">What Is a Semantic Layer ? | Dremio</a></li>

</ul>
</details>

**Tags**: `#text-to-SQL`, `#AI agents`, `#data quality`, `#LLM observability`, `#business intelligence`

---

<a id="item-19"></a>
## [Silicon Valley’s Shift From Innovation to Financialization](https://www.oreilly.com/radar/what-happened-to-silicon-valley/) ⭐️ 6.0/10

O’Reilly Radar examines how Silicon Valley’s incentive structures and culture shifted from technology-driven innovation toward shareholder value, aggressive growth, and financialization. The analysis links this transformation to venture-capital incentives, corporate governance, and the industry’s embrace of financial objectives. 这种转变影响科技公司如何配置资本、评估风险和定义成功，并波及初创企业、员工、投资者及更广泛的科技生态。文章还把硅谷当前的 AI 支出热潮置于一种更长的历史之中，即奖励规模扩张而非持久技术进步的激励机制。 A central mechanism discussed is ZIRP-era cheap capital, which enabled companies to grow to enormous scale and encouraged founders to pursue large markets rather than compete in established ones. As interest rates returned, commenters argued that companies began cannibalizing core capabilities to fund AI, raising questions about whether markets will penalize reckless spending.

hackernews · Hacker News \(热门\) · Nov 22, 19:20 · [Discussion](https://news.ycombinator.com/item?id=50602947)

**Background**: Silicon Valley remains a major center of technology investment and startup formation, with the region dominating U.S. tech funding and unicorn creation. Financialization generally describes the growing importance of financial markets and financial objectives within an economy or industry. In venture capital, rapid growth and large exit valuations can strongly shape how founders and investors set company strategy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Financialization">Financialization - Wikipedia</a></li>
<li><a href="https://www.ipaglobal.com/news/article/capital-project-trends-2026/">6 Big Trends Shaping the Future of Capital Projects | IPA</a></li>
<li><a href="https://fastercapital.com/content/The-Venture-Capital-Incentive-That-Drives-Success.html">The Venture Capital Incentive That Drives Success - FasterCapital</a></li>

</ul>
</details>

**Discussion**: Comments largely accepted the article’s critique while adding several possible explanations, including ZIRP-era incentives, the return of interest rates, AI spending, VC influencer culture, and a lack of purpose. One commenter argued that governance requires rebuilding the institutional “machine” around human flourishing, while another countered that Silicon Valley has always resembled its present culture and that only its circumstances have changed.

**Tags**: `#Silicon Valley`, `#venture capital`, `#capitalism`, `#tech industry`, `#financialization`

---

<a id="item-20"></a>
## [Sandwich Simulator Turns Layering Into Playful Web Interaction](https://stulle.app/) ⭐️ 6.0/10

Stulle.app presents an interactive web application in which users assemble and simulate elaborate sandwiches, drawing attention through a popular Hacker News discussion. The project combines a culinary theme with interactive visual behavior rather than offering a conventional restaurant-management game. The simulator illustrates how a simple, humorous subject can demonstrate polished interaction design and attract substantial community engagement. It is primarily an entertainment and creative-coding project, so its significance lies more in web experimentation and audience interest than in technological or scientific advances. The application supports the construction of visually elaborate sandwiches, with individual community examples and shared links contributing to its replay value. Suggested improvements include adding a top bread layer and allowing the finished sandwich to be cut in half; the available material provides no detailed information about its rendering technology, physics implementation, or development stack.

hackernews · Hacker News \(热门\) · Nov 22, 00:07 · [Discussion](https://news.ycombinator.com/item?id=50594911)

**Background**: A web simulator is an interactive application that visually represents a process, system, or object directly in a browser. In this case, sandwich assembly provides a playful setting for exploring layered visual construction and simulated food behavior, although the supplied material does not establish whether the movements use rigid-body physics, animation, or another technique.

<details><summary>References</summary>
<ul>
<li><a href="https://eshraqism.com/blog/stulle-app-the-sandwich-simulator-redefining-web-interaction-design">Stulle.app Sandwich Simulator: Web Design Masterclass ...</a></li>
<li><a href="https://portfolio-bay-pi-91.vercel.app/">FERUZ — Creative Developer &amp; Technologist</a></li>

</ul>
</details>

**Discussion**: The Hacker News comments are broadly playful and appreciative, praising both the simulator and the long history of simulated food on the web. Participants shared related sandwich projects and creative combinations, while also suggesting features such as adding bread on top and cutting the completed sandwich in half.

**Tags**: `#Web Simulation`, `#Interactive App`, `#Creative Coding`, `#Hacker News`, `#Sandwiches`

---

<a id="item-21"></a>
## [Backblaze Users Question Updated Data Sale and Sharing Terms](https://www.neowin.net/news/backblaze-customers-worried-of-personal-data-salesharing-after-policy-update/) ⭐️ 6.0/10

Backblaze updated its privacy documentation, prompting customers to question whether their personal data may be sold or shared. No data breach or confirmed policy violation was reported; the concern centers on the wording and scope of the disclosure. The change affects cloud-backup customers who may assume that service operators cannot use their uploaded files or associated personal information for unrelated commercial purposes. Clearer boundaries and client-side encryption could reduce uncertainty, although policy interpretation and real-world enforcement remain important distinctions. Backblaze&\#x27;s personal backup service is advertised at $9 per month for unlimited cloud storage, but search results note that it does not provide client-side encryption for files. Community suggestions include rclone crypt, Cryptomator, and restic, although a commenter says Backblaze excludes backup content from the sale-or-sharing categories described in the policy.

hackernews · Hacker News \(热门\) · Nov 22, 15:16 · [Discussion](https://news.ycombinator.com/item?id=50600435)

**Background**: A privacy policy generally defines what information a company collects, how it uses that information, and whether it discloses it to third parties or sells it. Cloud providers commonly apply server-side encryption, but client-side encryption occurs before upload, preventing the provider from reading file contents. The legal meaning of terms such as “sale” and “sharing” can depend on the jurisdiction and may include sharing for advertising or analytics rather than a cash sale.

<details><summary>References</summary>
<ul>
<li><a href="https://www.backblaze.com/cloud-backup/personal">Unlimited Cloud Backup for Mac &amp; PC | Backblaze — $9/Month</a></li>
<li><a href="https://www.cloudwards.net/best-online-backup-for-linux/">Linux Cloud Backup : The Best Online Backup Options in 2026</a></li>
<li><a href="https://proton.me/blog/zero-knowledge-cloud-storage">What is zero-knowledge cloud storage? - Proton Best Encrypted Cloud Storage 2026 - Zero-Knowledge Cloud Storage With Encryption in 2026: 5 Services Tested Best Encrypted Cloud Storage in 2026: Secure File Storage ... Best Encrypted Cloud Storage - BestBackupReviews.com What Is Zero-Knowledge Encryption? Why It Matters for Backup</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some considered the wording alarming and recommended client-side encryption as a hard requirement, while others said the reaction was excessive because backup content is excluded and the change may reflect broad legal definitions of data sharing. Participants also questioned whether the policy referred to third-party analytics and advertising disclosures rather than the sale of users&\#x27; backup files.

**Tags**: `#data-privacy`, `#cloud-backup`, `#encryption`, `#Backblaze`, `#security-policy`

---

<a id="item-22"></a>
## [Has Software Always Been Too Complex for Humans?](https://anil.recoil.org/notes/software-too-complex-for-humans) ⭐️ 6.0/10

The article examines the proposition that software complexity has persistently exceeded the limits of reliable human comprehension and management. Rather than reporting a product launch or new technical result, it offers a philosophical and technical inquiry grounded in the long-running difficulty of maintaining increasingly interconnected systems. If software has always exceeded human cognitive limits, better engineering practices alone may not be sufficient; teams may need to redesign systems, interfaces, and development processes around human constraints. The issue directly affects maintainability, technical debt, and the reliability of software used by businesses and consumers. Software metrics do not consistently predict how comprehensible a program will be to developers, because complexity and human understanding are related but distinct concepts. The article&\#x27;s framing should therefore be treated as an argument and research question, not as a newly established theorem or an empirical finding presented in the supplied content.

rss · Hacker News \(热门\) · Nov 22, 17:32

**Background**: Software complexity encompasses structural properties such as interconnected components, difficult control flow, and accumulated layers of changes. Research on software evolution highlights the difficulty of maintaining flexible systems as complexity grows, while studies of software comprehension caution that conventional complexity metrics do not always map neatly onto human understanding. More recent work on a cognitive horizon similarly frames human comprehension of advanced AI systems as bounded by fundamental cognitive constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/chapter/edited-volume/pii/B9780444705365500105">Software Comprehension - ScienceDirect</a></li>
<li><a href="https://www.researchgate.net/publication/315730051_Exploring_Complexity_in_Software_Systems_-_From_an_irrational_model_of_software_evolution_to_a_theory_of_psychological_complexity_and_cognitive_limitations_based_on_empirical_evidence">(PDF) Exploring Complexity in Software Systems - From an ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s43681-025-00846-x">Approaching the cognitive horizon: recognizing the limits of ...</a></li>

</ul>
</details>

**Tags**: `#software-engineering`, `#software-complexity`, `#systems-design`, `#programming`

---

<a id="item-23"></a>
## [C++26 Technical Work Completed After Second Review](https://herbsutter.com/2026/11/21/c26-is-done-again-trip-report-november-2026-iso-c-standards-meeting-buzios-brazil/) ⭐️ 6.0/10

The ISO C++ committee said it completed the technical work needed for C++26 for a second time during its November 2026 meeting in Búzios, Brazil. The meeting was conducted in a hybrid format, with remote participation through Zoom. C++26 is the next international standard for a language widely used in systems, infrastructure, desktop, and embedded software. Reaching this technical milestone advances the standard toward its final approval and publication process, although implementation by compiler vendors will remain a separate and potentially lengthy task. The committee had already completed the standard&\#x27;s technical work during its March meeting, making this the second completion milestone. The November meeting took place in Búzios, Rio de Janeiro, Brazil, and included both in-person and Zoom participation; the supplied material does not identify specific adopted features or implementation status.

rss · Lobsters \(技术社区\) · Nov 21, 13:57

**Background**: ISO/IEC JTC1/SC22/WG21 is the international working group responsible for standardizing C++. Its meetings review proposed language and library changes and advance the draft standard through the ISO process; the group also maintains committee information and technical reports. The supplied search results confirm the November 2026 technical completion but do not provide a feature-by-feature specification.

<details><summary>References</summary>
<ul>
<li><a href="https://herbsutter.com/2026/11/21/c26-is-done-again-trip-report-november-2026-iso-c-standards-meeting-buzios-brazil/">C++26 is done (again)! — Trip report: November 2026 ISO C++ ...</a></li>
<li><a href="https://open-std.org/jtc1/sc22/wg21/">ISO /IEC JTC1/SC22/WG21 - The C++ Standards Committee - ISOCPP</a></li>

</ul>
</details>

**Tags**: `#C++26`, `#ISO C++`, `#standards`, `#programming languages`

---

<a id="item-24"></a>
## [Mathematicians React to a Future AI Proof of GRH](https://www.youtube.com/watch?v=zqzk43bSdDI) ⭐️ 6.0/10

A video compilation brings together mathematicians’ responses to a hypothetical scenario in which AI produces a Lean-verified proof of the Riemann hypothesis that humans cannot understand. The video draws on interviews conducted over the past year and a half about AI in mathematics. The scenario highlights a central tension in AI-assisted mathematics: machine-checkable correctness may not guarantee human understanding, explanation, or insight. It also raises questions about how the field would interpret, communicate, and build on a formally verified result that experts cannot independently understand. Lean is a proof assistant and programming language that supports dependent types, type classes, an expressive tactic language, and formally verified code. The premise concerns automated theorem proving for the Riemann hypothesis, but the provided description gives no technical details about the hypothetical proof, its formalization, or how Lean verification would be achieved.

rss · Lobsters \(技术社区\) · Nov 22, 16:37

**Background**: Automated theorem proving is a field of automated reasoning and mathematical logic in which computer programs prove mathematical theorems. Lean can formally verify proofs and programs, providing strong machine-checkable guarantees, although such verification does not by itself establish that humans grasp the underlying argument. The Riemann hypothesis states that all nontrivial zeros of the zeta function have real part one-half, and remains an unresolved problem in this news context.

<details><summary>References</summary>
<ul>
<li><a href="https://lean-lang.org/">Lean Programming Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The provided content links to a discussion page but includes no comments or viewpoints from that discussion. The video itself reportedly features mathematicians’ reactions, but their specific arguments are not transcribed in the supplied material.

**Tags**: `#AI for mathematics`, `#automated theorem proving`, `#Lean`, `#Riemann hypothesis`, `#mathematics`

---

<a id="item-25"></a>
## [NixOS Bring-Up on Alibaba RISC-V Board](https://feyor.sh/blog/nixos-bringup-on-an-alibaba-riscv-board/) ⭐️ 6.0/10

The article documents the practical work of enabling and configuring NixOS on an Alibaba RISC-V development board. It focuses on a hardware bring-up process rather than a new product or major software release. A working NixOS setup can provide developers with a reproducible environment for experimenting with RISC-V and embedded Linux. The effort also highlights the practical gaps involved in supporting less-common processor architectures and boards. RISC-V bring-up commonly involves firmware, bootloader, kernel, and device-tree configuration before userspace tools become available. NixOS cross-compilation can use QEMU for testing, although emulation may reduce performance compared with native execution.

rss · Lobsters \(技术社区\) · Nov 22, 00:30

**Background**: NixOS is a Linux distribution built around declarative, reproducible package and system configuration. On RISC-V boards, developers must account for the board&\#x27;s processor, firmware and bootloader support, kernel configuration, and hardware description. Alibaba&\#x27;s T-Head TH1520 is a RISC-V system-on-chip used by development boards and has been supported in Fedora-based desktop-oriented efforts.

<details><summary>References</summary>
<ul>
<li><a href="https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head">Architectures/RISC-V/T-Head - Fedora Project Wiki</a></li>
<li><a href="https://wiki.nixos.org/wiki/Cross_Compiling">Cross compiling - Official NixOS Wiki</a></li>
<li><a href="https://lucaberton.com/blog/risc-v-boot-flow-opensbi-uboot-firmware/">RISC-V Boot Flow: OpenSBI, U - Boot &amp; the SBI | Luca Berton</a></li>

</ul>
</details>

**Tags**: `#NixOS`, `#RISC-V`, `#Linux`, `#embedded systems`, `#hardware bring-up`

---

<a id="item-26"></a>
## [Monitor Reportedly Cut Download Speed by 75%](https://blog.tymscar.com/posts/studiodisplayethernet/) ⭐️ 6.0/10

A technical troubleshooting post reports that a monitor was apparently reducing network download speeds by 75%. The supplied content contains only a link to a discussion, so the specific hardware, configuration, cause, and remedy cannot be verified from the available material. The case suggests that an apparently unrelated display device may affect network performance, making it important to diagnose the full hardware and cabling setup rather than assume the source server is at fault. If confirmed, the report could provide a useful example of how interface negotiation or physical interference can create a large, measurable throughput loss. The reported figure is a 75% reduction in download speed, but the available material gives no baseline throughput, test method, operating system, network interface, or monitor model. General Ethernet guidance recommends checking negotiated link speed, duplex mode, cabling, and interface error counters when throughput is unexpectedly low.

rss · Lobsters \(技术社区\) · Nov 21, 15:03

**Background**: Ethernet devices normally negotiate speed and duplex with the connected network equipment, and a mismatch or marginal physical connection can sharply reduce throughput. Because the original post’s full technical content is unavailable here, the search results only establish standard troubleshooting concepts and do not substantiate the claimed monitor-specific cause.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html">Configure and Verify Ethernet 10/100/1000Mb Half/Full Duplex ...</a></li>
<li><a href="https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Troubleshooting_and_Support/Troubleshooting/Duplex_mismatches_affecting_physical_link_speed">Troubleshooting Duplex Mismatches Affecting Physical Link Speed</a></li>
<li><a href="https://mikrotikdocs.fyi/interfaces/ethernet-interfaces/">Ethernet Interface Configuration | MikroTik RouterOS Docs</a></li>

</ul>
</details>

**Tags**: `#networking`, `#Ethernet`, `#monitoring`, `#troubleshooting`, `#hardware`

---

<a id="item-27"></a>
## [Local Web Tool Plans City Radio Mesh Networks](https://meshcoveragecalculator.lalala.ing/) ⭐️ 6.0/10

A local-first WebAssembly calculator estimates radio-link placement and the number of nodes needed for city-scale mesh networks. It combines FSPL and Delta-Bullington propagation models with terrain information and is seeking early design feedback. The tool could make mesh-network planning more accessible by helping communities estimate coverage and infrastructure requirements before deploying nodes. It also offers a privacy-friendly alternative to relying on hosted planning services, although its real-world accuracy and adoption remain unproven. The calculator runs locally in the browser through WASM and uses FSPL for free-space path loss plus Delta-Bullington for irregular-terrain propagation. Its model requires relevant inputs such as terrain elevation, antenna positions and heights, operating frequency, and polarization; actual deployment accuracy will still depend on real-world clutter, antenna characteristics, and environmental conditions.

rss · Lobsters \(技术社区\) · Nov 22, 18:17

**Background**: FSPL estimates radio-signal attenuation over an unobstructed path as a function of distance and frequency, but it does not account for buildings, vegetation, or terrain. Delta-Bullington adds terrain-profile analysis for radio propagation over irregular terrain and is discussed in ITU-R Recommendation P.526-15. A mesh network extends coverage through multi-hop links, so planners must evaluate both individual link viability and the arrangement of nodes needed to reach target areas.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Free-space_path_loss">Free-space path loss - Wikipedia</a></li>
<li><a href="https://erdc-library.erdc.dren.mil/items/1992d9ae-d068-4207-a9e6-53ed4ef6e888/full">A study on the Delta-Bullington irregular terrain ...</a></li>
<li><a href="https://meshtastic.org/docs/software/site-planner/">Meshtastic Site Planner</a></li>

</ul>
</details>

**Discussion**: The linked discussion is framed as an open request for feedback on whether the planning idea and its approach make sense. The available material does not provide enough comment text or sentiment data to summarize broader community reactions.

**Tags**: `#mesh-networks`, `#radio-propagation`, `#network-planning`, `#WASM`, `#Meshtastic`

---

<a id="item-28"></a>
## [GhostScript Upload2Shell Vulnerability Draws Security Attention](https://pwn.ai/upload2shell/research.html) ⭐️ 6.0/10

Researchers associated with pwn.ai published research on CVE-2026-125396, a GhostScript vulnerability dubbed “Upload2Shell,” with links to its research hub and NVD record. The original post itself mainly directs readers to those references and community discussion rather than presenting a full technical analysis. GhostScript is widely used behind file-processing services, including PDF preview, printing, document conversion, and upload workflows, so an exploitable vulnerability can affect many downstream applications. Search results describe the issue as a sandbox escape that may allow crafted files to execute server commands, potentially turning otherwise routine uploads into remote code execution. The cited research identifies CVE-2026-125396 as the public identifier for the “Upload2Shell” issue. Separate reporting also discusses a critical GhostScript heap buffer overflow fixed in GhostScript 10.08.0 on September 8, 2026, but the supplied material does not establish whether that finding is the same underlying vulnerability or a related issue.

rss · Lobsters \(技术社区\) · Nov 22, 00:52

**Background**: GhostScript interprets and processes documents such as PDFs and PostScript files, often as a hidden component in servers and desktop applications. A sandbox escape means code running through a crafted document can gain capabilities beyond the restrictions intended for file processing, and the name “Upload2Shell” emphasizes the risk when untrusted files are automatically processed.

<details><summary>References</summary>
<ul>
<li><a href="https://pwn.ai/upload2shell">Upload 2 Shell · CVE - 2026 - 125396 · pwn.ai research</a></li>
<li><a href="https://thehackernews.com/2026/11/researchers-demonstrate-ghostscript.html">Researchers Demonstrate Ghostscript Sandbox-Escape RCE via...</a></li>
<li><a href="https://www.wordfence.com/blog/2026/10/wordfence-argus-discovers-critical-vulnerability-in-ghostscript-the-program-that-turns-uploaded-pdfs-into-thumbnails-on-your-server/">Wordfence Argus Discovers Critical Vulnerability in Ghostscript , the...</a></li>

</ul>
</details>

**Discussion**: The post links to a Lobsters discussion about CVE-2026-125396, but no comments or viewpoints are included in the supplied content, so the community&\#x27;s sentiment cannot be assessed.

**Tags**: `#GhostScript`, `#CVE-2026-125396`, `#vulnerability research`, `#security`

---

<a id="item-29"></a>
## [OpenAI Scientist Proposes Measuring AI Development Speed](https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/) ⭐️ 6.0/10

OpenAI Chief Scientist Jakub Pachocki argued on November 22, 2026, that governing AI development requires a shared method for measuring its pace. He reportedly released internal perplexity measurements and proposed shared frontier-AI development limits tied to safety milestones. AI speed limits cannot be implemented consistently unless laboratories, researchers, and regulators can agree on what development speed means and how to track it. A shared measurement framework could make risk governance more coordinated, while also creating disputes over which indicators should determine when development must slow. The proposal uses perplexity measurements as part of the technical basis for comparing AI development progress, although the excerpt provides little detail about the exact formula, validation, or enforcement mechanism. The available reporting also warns that alignment and monitoring research may not advance as quickly as frontier AI capabilities.

rss · TechCrunch AI · Nov 22, 21:14

**Background**: AI development speed limits are intended to slow capability progress when laboratories cannot evaluate or mitigate new risks quickly enough. Measuring that speed is technically difficult because progress can involve model capabilities, research iteration, compute scaling, tool use, and autonomous workflows rather than a single benchmark. Broader AI governance research emphasizes proactive, inclusive, and adaptive rules that respond to rapid technological change without overlooking innovation, access, and risk.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unite.ai/openai-proposes-shared-ai-development-limits-tied-to-safety-milestones/">OpenAI Proposes Shared AI Development Limits Tied to Safety ...</a></li>
<li><a href="https://www.itu.int/epublications/publication/the-annual-ai-governance-report-2025-steering-the-future-of-ai">The Annual AI Governance Report 2025: Steering the Future of AI</a></li>
<li><a href="https://arxiv.org/pdf/2505.05541">Safety by Measurement: A Systematic Literature Review of AI ...</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#AI safety`, `#OpenAI`, `#AI policy`

---

<a id="item-30"></a>
## [Nvidia’s Earnings Contrast With Pressure for Huang’s Return](https://techcrunch.com/2026/11/21/a-tale-of-two-nvidias/) ⭐️ 6.0/10

Nvidia’s latest financial results portray a company with strong operating momentum, even as technology executives publicly urged CEO Jensen Huang to return. The article frames these as two sharply different signals surrounding Nvidia’s leadership and future direction. Nvidia remains central to the AI chip industry, where demand for data-center processors shapes suppliers, cloud infrastructure spending, and capital allocation. Huang’s leadership influence, combined with investor and employee support for his possible return, adds succession uncertainty to a company that continues to benefit from AI demand. Blackwell is Nvidia’s GPU architecture for AI and floating-point workloads and uses two dies connected by a 10 TB/s chip-to-chip interconnect. However, the supplied excerpt contains no detailed earnings figures, named executives, or specific arguments for Huang’s return, so its technical and financial conclusions remain limited.

rss · TechCrunch AI · Nov 21, 21:07

**Background**: Nvidia designs GPUs used in AI data centers, with Blackwell serving as the successor to Hopper and Ada Lovelace. Its latest architecture employs fifth-generation Tensor Cores and connects two reticle-limited dies through a 10 TB/s interconnect. Leadership at Nvidia carries unusual strategic importance because the company’s AI processors have made it a major beneficiary of industry-wide demand for training and inference infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/">The Engine Behind AI Factories | NVIDIA Blackwell Architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_%28microarchitecture%29">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.npr.org/2026/11/12/nx-s1-6037833/jensen-huang-nvidia-stepped-down">Nvidia CEO Jensen Huang resigns amid spy scandal : NPR</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#Jensen Huang`, `#Semiconductors`, `#AI Industry`, `#Earnings`

---

<a id="item-31"></a>
## [AI Face Licensing Tests Hollywood’s Future](https://techcrunch.com/2026/11/21/is-selling-an-ai-version-of-your-face-to-this-microdrama-startup-the-future-of-hollywood/) ⭐️ 6.0/10

An actor licensed his face to the microdrama startup Avni, which used his likeness to create a digital avatar for an entirely AI-generated project. The arrangement reflects a likeness-licensing trend already established in China and could expand in Hollywood. Licensing digital doubles could let actors appear in multiple low-cost productions without performing in each one, while giving studios access to reusable synthetic performers. If the model spreads, it could alter production economics, casting, compensation, and the ownership and control of actors’ likenesses. Avni’s wholly AI project used the actor’s licensed face to construct a digital avatar of him; the source material does not specify the license’s financial terms, duration, or rights provisions. The broader model remains constrained by consent, transparency, reuse limits, and the risk that synthetic performances may mislead audiences.

rss · TechCrunch AI · Nov 21, 16:00

**Background**: Microdramas are short-form series designed for mobile viewing, and Chinese producers have adopted generative AI to produce them faster and at a lower cost. A digital likeness is a synthetic representation of a real person’s appearance and voice, which can be reused without the person physically performing every scene. Prior cases involving synthetic versions of performers’ faces have raised concerns about consent, compensation, and unauthorized use.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/21/is-selling-an-ai-version-of-your-face-to-this-microdrama-startup-the-future-of-hollywood/">Is selling an AI version of your face to this microdrama ... | TechCrunch</a></li>
<li><a href="https://www.cnn.com/2026/08/22/style/short-drama-ai-china-intl-hnk">Quiet on set. How AI transformed China’s microdrama scene</a></li>
<li><a href="https://www.theguardian.com/technology/2024/oct/16/its-not-me-its-just-my-face-the-models-who-found-their-likenesses-had-been-used-in-ai-propaganda">‘It’s not me, it’s just my face’: the models who found their likenesses ...</a></li>

</ul>
</details>

**Tags**: `#generative-ai`, `#digital-likeness`, `#media-licensing`, `#microdrama`, `#hollywood`

---

<a id="item-32"></a>
## [GLP-1 Drugs Could Free Farmland Larger Than Italy](https://arstechnica.com/health/2026/11/glp-1-drugs-could-have-a-surprisingly-large-environmental-payoff/) ⭐️ 6.0/10

The analysis argues that GLP-1 drugs could reduce food demand enough to free agricultural land exceeding Italy’s total area. This would potentially lower pressure to cultivate additional land while producing environmental benefits. If sustained and widely adopted, lower food demand could reshape agricultural land use, food systems, and associated greenhouse gas emissions. The finding links public-health treatments to climate and land-use outcomes beyond individual weight loss. GLP-1 receptor agonists promote weight loss by suppressing appetite, increasing satiety, and delaying gastric emptying, which can reduce food consumption. The estimate depends on assumptions about treatment uptake, dietary behavior, agricultural responses, and how much land would actually be retired or restored, although the supplied description gives limited methodological detail.

rss · Ars Technica · Nov 22, 12:07

**Background**: Land sparing means meeting food demand without expanding the area of cultivated land, potentially allowing existing farmland to be restored or shared through lower-intensity production. WRI estimates that reducing global food loss and waste by 25% could narrow the projected land-use gap by 27% and the greenhouse gas mitigation gap by 15%, illustrating how demand-side changes can affect agriculture’s environmental footprint.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0002934325000592">Mechanisms of GLP-1 Receptor Agonist-Induced Weight Loss: A ...</a></li>
<li><a href="https://research.wri.org/wrr-food/course/reduce-growth-demand-food-and-other-agricultural-products-synthesis">Course 1: Reduce Growth in Demand for Food and other ... - WRI</a></li>
<li><a href="https://link.springer.com/article/10.1007/s41130-026-00262-7">To what extent can farmers spare or share land to meet food ...</a></li>

</ul>
</details>

**Tags**: `#GLP-1`, `#food systems`, `#environmental impact`, `#agriculture`, `#public health`

---

<a id="item-33"></a>
## [Meta Reconsiders 2030 Net-Zero Goal as AI Emissions Rise](https://arstechnica.com/ai/2026/11/meta-reconsiders-2030-net-zero-goal-amid-record-emissions-from-ai-data-centers/) ⭐️ 6.0/10

Meta is re-evaluating its 2030 sustainability goals in response to rising emissions associated with its expanding AI data-center infrastructure. The announcement signals a potential adjustment to a previously stated climate commitment. Meta’s review could influence how other technology companies reconcile rapid AI infrastructure expansion with emissions-reduction pledges. It also highlights growing pressure on data-center operators as electricity demand and carbon costs increase. The available report provides no revised target, implementation timetable, emissions figures, or specific policy changes for Meta. Net zero generally means reducing emissions as far as possible and using carbon-removal credits to offset residual emissions.

rss · Ars Technica · Nov 20, 21:47

**Background**: AI training and inference require energy-intensive computing hardware, servers, cooling systems, and supporting facilities, causing data-center electricity consumption to rise rapidly. MIT Technology Review reported that data-center electricity consumption had doubled by 2023 and represented about 4.4% of total U.S. energy use. These trends are challenging corporate net-zero commitments as technology companies race to expand AI capacity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2025/05/20/1116327/ai-energy-usage-climate-footprint-big-tech/">We did the math on AI ’s energy footprint. | MIT Technology Review</a></li>
<li><a href="https://www.aljazeera.com/news/2026/11/20/meta-rethinks-2030-climate-goals-as-ai-data-centres-drive-emissions-up">Meta rethinks 2030 climate goals as AI data centres drive emissions up</a></li>
<li><a href="https://www.deeplearning.ai/the-batch/ai-and-data-center-boom-challenges-big-techs-emissions-targets">AI and Data Center Boom Challenges Big Tech&#x27;s Emissions Targets</a></li>

</ul>
</details>

**Tags**: `#Meta`, `#AI infrastructure`, `#data centers`, `#emissions`, `#sustainability`

---

<a id="item-34"></a>
## [Isaac Developer Removes AI Music After Backlash](https://www.theverge.com/games/1039770/binding-of-isaac-ai-music) ⭐️ 6.0/10

The developer of The Binding of Isaac: Repentance Plus removed AI-generated music from the expansion after Steam users discovered Suno metadata in several audio files. The tracks appeared in a Grand Theft Auto-themed section and their undisclosed use prompted a wave of negative reviews. The episode illustrates how undisclosed AI-generated assets can cause immediate backlash against commercial games, even when the affected content is limited to a small segment. It highlights the importance of disclosure and how player coordination on Steam can rapidly affect a product&\#x27;s public reputation. Reddit user ShweetsStuff identified the AI music by finding Suno metadata in the game&\#x27;s audio files and linking the tracks to the Grand Theft Auto-themed section. Steam&\#x27;s review-bombing systems can flag or restrict reviews when coordinated campaigns target unrelated issues, such as undisclosed content practices.

rss · The Verge · Nov 22, 17:25

**Background**: Suno is an AI music generator that can create complete songs—including vocals, lyrics, and production—from a text prompt. Steam review bombing occurs when owners coordinate a large volume of negative or positive reviews to influence a game&\#x27;s visibility and public perception. The controversy here centers on whether the developer sufficiently disclosed the use of AI-generated music.

<details><summary>References</summary>
<ul>
<li><a href="https://suno.com/">Suno | AI Music Generator</a></li>
<li><a href="https://en.wikipedia.org/wiki/Review_bomb">Review bomb - Wikipedia</a></li>
<li><a href="https://store.steampowered.com/curator/36308017-Review-Bomb-Tracking-Off-Topic/">Steam Curator: Review Bomb Tracking / Off Topic</a></li>

</ul>
</details>

**Discussion**: Players responded to the discovery by review-bombing Repentance Plus on Steam, expressing strong opposition to undisclosed AI-generated content. The backlash led the developer to remove the affected music rather than defend its inclusion.

**Tags**: `#AI-generated music`, `#game development`, `#Steam`, `#player backlash`, `#content disclosure`

---

<a id="item-35"></a>
## [Sterilized Soil Kept Lifelike Reactions Alive for Six Years](https://www.wired.com/story/scientists-tried-to-kill-this-dirt-but-it-wouldnt-die/) ⭐️ 6.0/10

Scientists found that biologically meaningful chemical reactions continued for six years in sterilized soil. The result may illuminate chemical processes that preceded and potentially enabled the origin of life on Earth. The finding suggests that soil chemistry alone can sustain reaction networks resembling those associated with life, even without living organisms. It could therefore offer astrobiologists new evidence for studying how prelife chemistry may have developed toward biological systems. The reported persistence lasted six years and involved chemically active, life-sustaining reactions rather than confirmed reproduction by living organisms. The available summary does not describe the sterilization method, reaction measurements, experimental replication, or criteria used to classify the reactions as biologically meaningful.

rss · Wired · Nov 22, 10:30

**Background**: Abiogenesis is the study of how chemical reactions gave rise to the first living systems under conditions different from those of modern Earth. Astrobiology examines whether chemical and environmental processes can help explain how life began, including the potential roles of minerals and soil in organizing or stabilizing reactive molecules. The discovery of sugars in meteorites also demonstrates that extraterrestrial environments can naturally produce some chemical ingredients associated with life.

<details><summary>References</summary>
<ul>
<li><a href="https://bleen.com.au/gallery/1072-sterile-soil-lifelike-biochemistry-abiogenesis.html">When Sterile Soil Acts Alive: What &#x27;Lifelike&#x27; | BLEEN</a></li>
<li><a href="https://en.wikipedia.org/wiki/Abiogenesis">Abiogenesis - Wikipedia</a></li>
<li><a href="https://astrobiology.nasa.gov/">Homepage | Astrobiology</a></li>

</ul>
</details>

**Tags**: `#origin-of-life`, `#astrobiology`, `#soil-microbiology`, `#chemical-reactions`, `#research`

---

<a id="item-36"></a>
## [Super El Niño Could Intensify Global Hunger](https://www.wired.com/story/how-this-years-super-el-nino-will-worsen-global-hunger/) ⭐️ 6.0/10

A powerful El Niño is approaching its peak, bringing severe drought to parts of Central America and other vulnerable regions. Combined with wars, reduced foreign aid, and disrupted access to energy and fertilizer, the event could leave millions without enough food. Climate hazards are compounding existing humanitarian crises rather than occurring in isolation. The combined effects on harvests, food prices, farm inputs, and aid capacity could sharply increase acute food insecurity in already vulnerable countries. The EU’s Joint Research Centre projects an 83% increase in people facing acute food insecurity in Central America, where El Niño-induced drought and record summer temperatures are damaging crops and threatening a second planting cycle. A super El Niño is a media term for a very strong event involving average sea-surface temperatures in parts of the Pacific rising by at least 2°C, though individual regions may experience either flooding or drought.

rss · Wired · Nov 22, 10:00

**Background**: El Niño is a phase of the naturally recurring El Niño–Southern Oscillation and alters global rainfall patterns by warming tropical Pacific waters. Its effects differ by location, with some regions becoming wetter while others experience prolonged drought. Very strong El Niño events can last for a year or more, making them especially damaging when harvests, markets, and humanitarian systems are already under pressure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/how-this-years-super-el-nino-will-worsen-global-hunger/">How This Year’s Super El Niño Will Worsen Global Hunger | WIRED</a></li>
<li><a href="https://scied.ucar.edu/learning-zone/climate-change-impacts/el-nino-strength">A Super El Niño Is Very Strong, But Even Weaker El Niños ...</a></li>
<li><a href="https://e360.yale.edu/features/super-el-nino-agriculture">How This Year&#x27;s Super El Niño Will Worsen Global Hunger - Yale E360</a></li>

</ul>
</details>

**Tags**: `#El Niño`, `#Climate Change`, `#Global Hunger`, `#Food Security`, `#Humanitarian Crises`

---

<a id="item-37"></a>
## [AI Accelerates the Race to Patch Vulnerabilities](https://www.wired.com/story/brace-yourself-for-years-of-outage-chaos/) ⭐️ 6.0/10

AI-assisted vulnerability discovery and automated exploit generation are shortening the time between finding a flaw and attacking systems that remain unpatched. Organizations are therefore under growing pressure to identify, prioritize, and repair vulnerabilities faster. Faster exploitation can turn routine software updates into operational emergencies, increasing the risk of outages, data breaches, and service disruption. Security teams and infrastructure operators may also face sustained pressure to keep pace with AI-enhanced attackers. AI tools can help locate vulnerabilities and generate working exploit code, reducing the time and expertise needed to weaponize flaws. However, available reporting also cautions that exploitation often trails disclosure, so it is too early to conclude that AI-assisted discovery automatically produces more successful attacks.

rss · Wired · Nov 21, 13:00

**Background**: A vulnerability is a weakness that attackers can exploit to compromise software or systems, while patching means applying a fix. AI can assist both defensive vulnerability discovery and offensive exploit generation, compressing the window defenders have to deploy a fix after a flaw becomes public. The searched race-condition results concern a separate class of timing bugs and are not evidence of the broader AI-driven patching trend described in the article.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/jeffburnett225_vulncheck-state-of-exploitation-1h-2026-activity-7488228095162949632-Nbl1">AI - assisted vulnerability discovery not leading to more... | LinkedIn</a></li>
<li><a href="https://www.oksim.ua/2024/10/17/dark-side-of-ai-in-cybersecurity/">Dark Side of AI in Cybersecurity - Oksim | Oksim - IT допомога</a></li>
<li><a href="https://www.imperva.com/learn/application-security/race-condition/">Race Condition Vulnerability | Causes, Impacts &amp; Prevention ...</a></li>

</ul>
</details>

**Tags**: `#AI-assisted cybersecurity`, `#vulnerability patching`, `#system outages`, `#exploit automation`, `#cybersecurity`

---

<a id="item-38"></a>
## [OpenAgentCore Brings a Self-Hosted OpenAI Agents API](https://github.com/MiniMax-AI/OpenAgentCore) ⭐️ 6.0/10

MiniMax released OpenAgentCore, an open-source and self-hostable implementation of the OpenAI Agents API. It lets developers run Codex, Claude Code, or MiniMax Code on their own machines, with their own models, through the official OpenAI SDK. The project gives developers greater control over deployment, execution environments, and model choices while preserving compatibility with the official OpenAI SDK. It could reduce infrastructure lock-in and make agent orchestration more suitable for private or customized environments. OpenAgentCore describes itself as an open-source, self-hosted implementation with multiple native harnesses and claims support for several coding-agent systems. The available evidence is still early: the Hacker News submission received one point and no comments, so broad adoption and production readiness are not demonstrated.

rss · Hacker News \(best\) · Nov 22, 21:18

**Background**: OpenAI’s Agents API is a managed interface for building agent applications, with OpenAI handling sessions, orchestration, context compaction, and recovery while applications supply tools and an execution environment. OpenAgentCore aims to provide a self-hosted alternative with a compatible programming interface. The official SDK allows applications to invoke supported agent harnesses without requiring every internal detail to be implemented independently.

<details><summary>References</summary>
<ul>
<li><a href="https://openagentcore.dev/">OpenAgentCore — One core. Many agents.</a></li>
<li><a href="https://openagentcore.dev/docs/architecture">Architecture | OpenAgentCore</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#open source`, `#self-hosting`, `#OpenAI API`, `#developer tools`

---

<a id="item-39"></a>
## [Three Controls for Recovery JWTs and JWKS Rotation](https://dev.to/rivenor85/account-recovery-jwt-evidence-with-3-controls-for-jwks-cache-rotation-2i85) ⭐️ 6.0/10

The article recommends verifying device-risk JWTs against explicitly trusted issuer, audience, algorithm, and time requirements, while retrieving signing keys through a bounded JWKS cache. It also advises retaining minimal recovery-decision evidence and treating risk scores as signals rather than proof of account ownership. These controls can prevent replayed or misdirected tokens from influencing sensitive account-recovery decisions and can reduce outages when signing keys rotate. They also minimize telemetry collection while preserving the distinction between a device-risk assessment and strong ownership proof. The verifier should configure the issuer, audience, permitted algorithms, and JWKS location outside the token; a token-supplied \`kid\` may select a candidate key but must not authorize an arbitrary key URL. Use a maintained JOSE implementation, enforce required time claims, and adopt bounded caching, refetching on an unknown key identifier where appropriate, and rate limiting.

rss · Dev.to · Nov 22, 21:24

**Background**: JWKS is a trusted issuer&\#x27;s published set of public keys used to verify JWT signatures, and key rotation requires clients to discover new keys without fetching them on every request. Device-risk services may issue a signed assessment that influences how strongly an account should be challenged, but the JWT proves only that the trusted service produced the assessment; it does not prove that browser observations are truthful or that the requester owns the account. Account recovery therefore still needs an appropriate ownership challenge, consistent responses, and single-use recovery tokens with expiration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.session-management.com/oidc-oauth-20-implementation/validating-jwts-and-rotating-signing-keys/caching-jwks-without-breaking-key-rotation/">Caching JWKS Without Breaking Key Rotation | session ...</a></li>
<li><a href="https://support.okta.com/help/s/article/best-practices-for-caching-the-okta-json-web-keys-set-jwks-for-oauth">Best Practices for Caching the Okta JSON Web Keys Set (JWKS ...</a></li>
<li><a href="https://www.cerberauth.com/blog/jwt-multi-issuer-validation/">Validating JWTs from Multiple Issuers | CerberAuth</a></li>

</ul>
</details>

**Tags**: `#JWT Security`, `#JWKS Caching`, `#Account Recovery`, `#Device Fingerprinting`, `#Node.js`

---

<a id="item-40"></a>
## [Role-Separated AI Agents for Safer Pull Request Review](https://dev.to/himanshu231204/live-coding-with-an-ai-team-a-safe-way-to-review-a-pr-one-writer-one-reviewer-one-publisher-170i) ⭐️ 6.0/10

The article presents a live-coding workflow in which Claude Code writes the fix, OpenCode independently reviews the exact diff without editing files, and a human decides whether to merge. It also assigns optional summary and narration roles to Hermes and ChatGPT dot, while restricting publishing to one authorized identity. Separating writing, reviewing, and publishing reduces conflicting edits, misleading handoffs, duplicate comments, and premature merge decisions. As AI coding agents increasingly generate and review pull requests independently, explicit permissions and human approval become important safeguards. The writer should use a clean Git worktree, and the reviewer should receive a saved diff generated between pinned base and target revisions. Findings should move from suspected to reproduced, only one identity should publish to GitHub, and narration should state the exact CI state rather than treating queued checks as passed.

rss · Dev.to · Nov 22, 21:23

**Background**: A Git worktree is another checkout of the same repository that lets an agent modify files without sharing the main working directory. Pull-request review requires comparing exact revisions so that comments target the code that will actually be published. The workflow reflects a human-in-the-loop pattern in which agents handle bounded tasks while people retain authority over consequential decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/code-review">Code Review by Claude | AI code review tool for pull requests</a></li>
<li><a href="https://code.claude.com/docs/en/code-review">Code Review - Claude Code Docs</a></li>
<li><a href="https://porteur.ai/guides/human-in-the-loop-ai-agents">Human in the Loop for AI Agents : Designing the Handoff ... | Porteur. ai</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Pull Request Review`, `#Software Engineering`, `#Human-in-the-Loop`, `#Developer Tools`

---

<a id="item-41"></a>
## [Inventory PDF.js Viewers by Origin, Not Product Name](https://dev.to/sorrelthorncroft/pdfjs-viewer-pages-need-origin-aware-inventory-not-a-library-version-claim-3fi6) ⭐️ 6.0/10

A methodology note argues that PDF.js viewer exposure should be mapped by embedding origin, deployment context, and page-content patterns rather than inferred from product-name matches or library versions. A fixed-date ZoomEye measurement on November 23, 2026 returned zero application matches, 431 title matches, and 2,530 body matches, all treated as discovery leads rather than confirmed vulnerabilities. Public viewer pages may omit PDF.js identifiers, while pages containing the product name can be harmless documentation portals, customer file links, or exposed internal applications. Mapping each viewer to its owner, origin, parent application, document source, and browser boundary provides a more actionable security inventory than a raw page count. The note recommends reviewing \`isEvalSupported\`, origin configuration, message handlers, document-URL wrappers, iframe sandboxing, CSP, package and worker versions, and parent-frame allowlists. It also recommends serving untrusted documents from a separate origin without application cookies or storage, and testing whether dangerous URLs or parent-frame access are blocked.

rss · Dev.to · Nov 22, 21:23

**Background**: PDF.js is a JavaScript PDF renderer that is frequently embedded inside another application, so its interface may expose only a document title, toolbar, or URL. Its viewer operates under the browser&\#x27;s same-origin policy, meaning browser permissions and the effective origin model determine what scripts and documents can access. Historical arbitrary-JavaScript behavior associated with eval-based execution underscores why current configuration must be inspected instead of relying on assumptions about an old release.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mozilla/pdf.js/">GitHub - mozilla/pdf.js: PDF Reader in JavaScript · GitHub</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy">Same - origin policy - Security | MDN</a></li>
<li><a href="https://portswigger.net/web-security/cors/same-origin-policy">Same - origin policy (SOP) | Web Security Academy</a></li>

</ul>
</details>

**Tags**: `#PDF.js`, `#web-security`, `#same-origin-policy`, `#measurement-methodology`, `#exposure-inventory`

---

<a id="item-42"></a>
## [Assisted Reproduction Amid Declining Fertility Rates](https://www.nejm.org/doi/full/10.1056/NEJMp2611049?ai=nejm&amp;af=R&amp;rss=currentIssue) ⭐️ 6.0/10

A New England Journal of Medicine perspective examines how assisted reproductive technology may respond to, mitigate, or reshape declining fertility rates. The available material identifies the topic but does not disclose the article&\#x27;s evidence, specific recommendations, or substantive conclusions. The analysis could connect reproductive medicine with demographic change and public-health policy as more societies experience fewer births and population aging. It may also clarify how expanded fertility care affects individuals facing infertility and broader population trends. Assisted reproductive technology includes procedures such as IVF, ICSI, fertility medication, and gamete or embryo cryopreservation. However, the supplied citation contains no extractable evidence or arguments, so the perspective&\#x27;s clinical scope, demographic model, limitations, and policy implications cannot be evaluated.

rss · NEJM · 最新文章 · Nov 21, 12:30

**Background**: Fertility rates have fallen across many societies during the demographic transition, contributing to slower population growth, aging populations, and in some countries, sustained population decline. Assisted reproductive technology is primarily used to treat infertility, with IVF being the most common form; the technology may help individuals realize desired pregnancies but cannot necessarily reverse population-level demographic decline.

<details><summary>References</summary>
<ul>
<li><a href="https://medlineplus.gov/assistedreproductivetechnology.html">Assisted Reproductive Technology | IVF | MedlinePlus Assisted Reproductive Technology (ART): Technique &amp; Types Assisted reproductive technology - Wikipedia IVF &amp; Assisted Reproductive Technology (ART) Guide Assisted Reproductive Technologies - Stanford Health Care About ART | ART | CDC</a></li>
<li><a href="https://ourworldindata.org/demographic-transition">Demographic transition : Why is rapid population ... | Our World in Data</a></li>
<li><a href="https://www.mckinsey.com/mgi/our-research/dependency-and-depopulation-confronting-the-consequences-of-a-new-demographic-reality">Confronting the consequences of a new demographic reality | McKinsey</a></li>

</ul>
</details>

**Tags**: `#fertility`, `#assisted reproductive technology`, `#demography`, `#public health`, `#reproductive medicine`

---

<a id="item-43"></a>
## [Health Professionals Urged to Support Detained Palestinian Colleagues](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2826%2902088-X/fulltext?rss=yes) ⭐️ 6.0/10

A Lancet correspondence calls on health professionals and their organizations to speak out about the dangerous conditions experienced by Palestinian health-care workers from Gaza and the West Bank in Israeli detention centers. The appeal places professional responsibility and advocacy at the center of responses to risks affecting detained medical personnel. Public statements by health organizations could increase attention to humanitarian and occupational-health concerns. The published content centers on health-care workers from Gaza and the West Bank held in Israeli detention centers. It is an advocacy statement rather than a clinical study or detailed technical assessment, and the excerpt does not specify the number of detainees, their medical conditions, or the detention period.

rss · The Lancet · 最新文章 · Nov 20, 23:30

**Background**: 《柳叶刀》的这封 Correspondence 强调，被拘押的巴勒斯坦医疗卫生工作者可能面临健康风险，并主张专业组织不应继续沉默。其论述体现了医学协会保护卫生工作者、提高公众对人道问题关注的职责。

**Tags**: `#medical ethics`, `#humanitarian health`, `#Gaza`, `#health professionals`, `#advocacy`

---