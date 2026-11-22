---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 139 items, 39 important content pieces were selected

---

1. [Perplexity as a Simple Progress Metric Toward Intelligence](#item-1) ⭐️ 9.0/10
2. [Anthropic’s 2028 Power Mix Could Be 98% Fossil Fuel](#item-2) ⭐️ 8.0/10
3. [C++26 Technical Work Completed in Brazil](#item-3) ⭐️ 8.0/10
4. [Four Escapes Show Why Containers Cannot Safely Host AI Agents](#item-4) ⭐️ 8.0/10
5. [What Happened to Silicon Valley? A Case for Mechanism Design](#item-5) ⭐️ 7.0/10
6. [Show HN: A Game Where Players Become LLM Subagents](#item-6) ⭐️ 7.0/10
7. [Japanese Automakers Standardize Parts to Cut Costs](#item-7) ⭐️ 7.0/10
8. [A Better Vocabulary for Software Testing](#item-8) ⭐️ 7.0/10
9. [Why Useless Knowledge Can Prove Profoundly Useful](#item-9) ⭐️ 7.0/10
10. [Localcode Brings One-Command Agentic Coding to macOS](#item-10) ⭐️ 7.0/10
11. [Two Million AI Canaries Expose Widespread Secret Leakage](#item-11) ⭐️ 7.0/10
12. [PostgreSQL Packaged as a Single Binary](#item-12) ⭐️ 7.0/10
13. [Microsoft 365 Outage Post-Incident Report](#item-13) ⭐️ 7.0/10
14. [GhostScript Upload2Shell Vulnerability Enables Remote Code Execution](#item-14) ⭐️ 7.0/10
15. [Muru Brings Rust-Powered Production Tooling to Python](#item-15) ⭐️ 7.0/10
16. [Signal Restricts Mobile Screenshots Against AI Surveillance](#item-16) ⭐️ 7.0/10
17. [Race Realism Misuses Genetics, Article Argues](#item-17) ⭐️ 7.0/10
18. [U.S. Banks Restrict Third-Party AI Agents](#item-18) ⭐️ 7.0/10
19. [Life’s Chemical Reactions Persisted in Sterilized Soil for Six Years](#item-19) ⭐️ 7.0/10
20. [AI Accelerates Exploits Beyond the Patch Window](#item-20) ⭐️ 7.0/10
21. [Typed Slot Memory Preserves Facts During Context Compaction](#item-21) ⭐️ 7.0/10
22. [AI Ported One Python Function to Rust for 78× Speedup](#item-22) ⭐️ 7.0/10
23. [Beginner’s Guide to Local AI with Inkling, Qwen, and Unsloth](#item-23) ⭐️ 6.0/10
24. [Alliance Proposes Shared Protocol for Open Social Media](#item-24) ⭐️ 6.0/10
25. [How BSD Escaped AT&amp;T&\#x27;s Unix Licensing](#item-25) ⭐️ 6.0/10
26. [Harvard Offers Graduate Course on AI Alignment and Safety](#item-26) ⭐️ 6.0/10
27. [Common Misconceptions About ATProto](#item-27) ⭐️ 6.0/10
28. [Gliver Completes the Guix Desktop Environment](#item-28) ⭐️ 6.0/10
29. [NixOS Brought Up on Alibaba RISC-V Board](#item-29) ⭐️ 6.0/10
30. [Open-Source Calculator Plans City-Scale Radio Mesh Networks](#item-30) ⭐️ 6.0/10
31. [Advice for the Next 100 Rust GUIs](#item-31) ⭐️ 6.0/10
32. [Sutskever Proposes Measurable AI Development Speed Limits](#item-32) ⭐️ 6.0/10
33. [Nvidia’s Earnings and Leadership Crisis](#item-33) ⭐️ 6.0/10
34. [AI Face Licensing Tests Hollywood’s Consent Boundaries](#item-34) ⭐️ 6.0/10
35. [Super El Niño Could Intensify Global Hunger](#item-35) ⭐️ 6.0/10
36. [ESA Probe Revisits NASA’s Asteroid Defense Test Site](#item-36) ⭐️ 6.0/10
37. [Large-Language-Model Pre-training Still Shows Scaling Gains](#item-37) ⭐️ 6.0/10
38. [When Postgres Cleanup Needs a Message Queue](#item-38) ⭐️ 6.0/10
39. [Shell-Injection Scanner Adds Signed, Auditable Reports](#item-39) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Perplexity as a Simple Progress Metric Toward Intelligence](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 9.0/10

OpenAI argues that falling language-model perplexity is a simple, meaningful indicator of progress toward intelligence. The claim challenges the prevailing emphasis on cross-entropy training objectives and reinforcement learning, and has prompted extensive technical debate about prediction, compression, and reasoning. A broadly comparable metric could make model progress easier to assess than sprawling benchmark suites, particularly when evaluating how well models learn regularities in data. However, perplexity does not by itself establish that specific cognitive abilities have emerged, so it must be interpreted alongside task-level evaluations. Perplexity measures how surprising a model finds the actual next tokens, given their preceding context; lower values indicate better prediction, with an ideal value of 1. For autoregressive language models, this metric is well defined, but it remains sensitive to the evaluation data and tokenization and may not transfer cleanly to masked language models or specialized capabilities.

hackernews · Hacker News \(热门\) · Nov 22, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50601525)

**Background**: Perplexity is derived from the average uncertainty a model assigns to the next token, and lower perplexity generally means that it predicts the evaluation sequence more accurately. It is commonly used to evaluate autoregressive or causal language models, but is not equally well defined for masked models. The discussion also connects prediction with compression: discovering regularities in data can reduce the information needed to represent it, while reasoning models complicate simple comparisons through post-training methods.

<details><summary>References</summary>
<ul>
<li><a href="https://www.baeldung.com/cs/language-models-perplexity">Evaluating Language Models Using Perplexity - Baeldung</a></li>
<li><a href="https://huggingface.co/docs/transformers/perplexity">Perplexity of fixed-length models - Hugging Face</a></li>
<li><a href="https://philarchive.org/archive/BOSTCO-17">The Collapse of Predictive Compression : Why Probabilistic...</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed perplexity as a simple benchmark and connected it to a longstanding view of intelligence as prediction and compression. Others were skeptical that particular abilities emerge at fixed perplexity thresholds, noting that specialized training can yield strong math performance despite weak general prediction, and emphasizing the need to match perplexity with task-specific data and evaluations.

**Tags**: `#language-model-evaluation`, `#perplexity`, `#AGI`, `#machine-learning-theory`, `#reasoning-models`

---

<a id="item-2"></a>
## [Anthropic’s 2028 Power Mix Could Be 98% Fossil Fuel](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/) ⭐️ 8.0/10

A Better Data Center Project case study projects that electricity serving Anthropic’s contracted US data centers could derive about 87% from natural gas and 11% from coal in 2028, leaving renewables at a negligible share. Its mid-case estimate also indicates annual emissions of roughly 17 million to 38 million metric tons of CO2 equivalent. The projection highlights how the rapid expansion of AI computing may add substantial fossil-fuel demand, local pollution, and grid pressure. It also raises questions about whether voluntary corporate commitments are sufficient without regulation that makes data centers account for their environmental and social costs. The analysis ties the estimate to about 15 gigawatts of contracted compute and sites using on-site gas turbines under “bring your own power” arrangements. These are projections rather than measured results, and the figures depend on the report’s assumptions about contracted facilities, generation sources, utilization, and grid conditions.

hackernews · Hacker News \(热门\) · Nov 22, 08:57 · [Discussion](https://news.ycombinator.com/item?id=50597612)

**Background**: AI models require large data centers, which consume electricity at a scale that can affect regional power systems and nearby communities. In some locations, data-center developers finance or contract dedicated generation instead of relying solely on the existing grid, while renewable-energy commitments may cover only a portion of a company’s broader electricity use. The analysis presents Anthropic as a case study in how the growth of AI infrastructure can be linked to fossil generation and additional emissions.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/anthropic-data-center-power-gas-coal-byop-2028-better-datacenter-november-2026">Anthropic Power Mix: 87% Gas, 11% Coal by 2028 (Study ...</a></li>
<li><a href="https://www.winzheng.com/en/article/anthropic-2028-energy-87-gas-11-coal-fossil-fuel-analysis">Anthropic’s 2028 Electricity to Be 87% Fossil Fuel: An ...</a></li>
<li><a href="https://www.euronews.com/2026/11/19/the-dark-side-of-ai-us-data-centres-emit-more-carbon-than-all-of-denmark">The dark side of AI : US data centres emit more carbon... | Euronews</a></li>

</ul>
</details>

**Discussion**: Commenters were strongly critical of Anthropic, citing local pollution around its Memphis operations, the absence of US renewable-energy commitments, and the failure of financial incentives to address climate externalities. Several argued that regulation is needed to shift environmental and social costs away from affected communities, while others questioned whether AI developers will voluntarily prioritize climate solutions amid the sector’s short-term profit incentives.

**Tags**: `#AI infrastructure`, `#data-center energy`, `#Anthropic`, `#climate impact`, `#energy policy`

---

<a id="item-3"></a>
## [C++26 Technical Work Completed in Brazil](https://herbsutter.com/2026/11/21/c26-is-done-again-trip-report-november-2026-iso-c-standards-meeting-buzios-brazil/) ⭐️ 8.0/10

The ISO C++ committee announced that it had completed the technical work for C++26 for a second time at its November 2026 meeting in Búzios, Brazil, with hybrid participation through Zoom. The meeting followed the committee’s earlier completion of C++26 technical work in March. Completion of the technical work marks a major milestone for C++ developers and toolchain implementers moving toward the next ISO-standardized release. It enables downstream work such as final publication, compiler and library implementation, and developer migration planning. The November meeting was held in Búzios, in the state of Rio de Janeiro, Brazil, and included hybrid online participation. The available material does not enumerate the final C++26 feature set or explain what “again” refers to beyond the earlier March completion.

rss · Lobsters \(技术社区\) · Nov 21, 13:57

**Background**: ISO C++ standards are developed through committee meetings and formal paper reviews before the finalized standard is published. C++26 is expected to include features associated with static reflection and contract programming, while hazard pointers are also discussed as part of the release’s broader technical direction. The announcement in this item concerns the committee’s technical completion milestone rather than a detailed feature summary.

<details><summary>References</summary>
<ul>
<li><a href="https://herbsutter.com/2026/11/21/c26-is-done-again-trip-report-november-2026-iso-c-standards-meeting-buzios-brazil/">C++26 is done (again)! — Trip report: November 2026 ISO C++ ...</a></li>
<li><a href="https://isocpp.org/files/papers/P2996R4.html">Reflection for C++26 - isocpp.org</a></li>
<li><a href="https://www.signalthirty.com/post/c26-new-features-reflection-contracts-and-more-explained">C++26 New Features: Reflection, Contracts, and More Explained</a></li>

</ul>
</details>

**Tags**: `#C++`, `#ISO Standards`, `#Language Evolution`, `#C++26`, `#Software Development`

---

<a id="item-4"></a>
## [Four Escapes Show Why Containers Cannot Safely Host AI Agents](https://dev.to/sandscale/four-container-escapes-and-what-they-teach-about-running-agent-code-2ak1) ⭐️ 8.0/10

The article synthesizes four public container-escape vulnerabilities—including runc flaws and the Linux &quot;Dirty Pipe&quot; kernel bug—to show how untrusted, model-generated code can cross a container boundary. It recommends stronger isolation practices for AI-agent infrastructure rather than treating a conventional container as a sufficient sandbox. AI agents may generate or select code from untrusted inputs, making containers a genuine security boundary rather than merely a packaging mechanism. Successful escapes could expose host filesystems, credentials, and other workloads, affecting organizations that deploy coding agents in production. The supplied excerpt details CVE-2019-5736, in which runc 1.0-rc6 and earlier could let a container overwrite the host runtime, and CVE-2024-21626, where a leaked file descriptor in runc 1.1.11 and earlier exposed the host filesystem and enabled binary replacement; runc 1.1.12 fixed the latter. Practical measures include running agent commands as unprivileged users, using user namespaces, treating agent-written Dockerfiles as attacker-controlled input, and adding isolation stronger than a shared-kernel container.

rss · Dev.to · Nov 22, 23:46

**Background**: Containers isolate processes through namespaces, controls, and a shared host kernel, making them fast and convenient but dependent on the runtime and kernel remaining secure. The excerpt also describes CVE-2022-0847, or &quot;Dirty Pipe,&quot; in which an improperly initialized Linux pipe-buffer flag allowed a local user to modify page-cache pages backed by read-only files and escalate privileges. Search results further emphasize that untrusted-code sandboxes may need layered controls, including restricted system calls or microVM-based isolation.

<details><summary>References</summary>
<ul>
<li><a href="https://unit42.paloaltonetworks.com/breaking-docker-via-runc-explaining-cve-2019-5736/">Breaking out of Docker via runC – Explaining CVE - 2019 - 5736</a></li>
<li><a href="https://blaxel.ai/blog/python-sandbox-llm-untrusted-code-isolation">Python Sandbox for LLM Code : MicroVM Isolation Guide | Blaxel Blog</a></li>
<li><a href="https://dev.to/mohameddiallo/4-ways-to-sandbox-untrusted-code-in-2026-1ffb">4 ways to sandbox untrusted code in 2026 - DEV Community</a></li>

</ul>
</details>

**Tags**: `#container-security`, `#AI-agents`, `#sandboxing`, `#vulnerabilities`, `#untrusted-code`

---

<a id="item-5"></a>
## [What Happened to Silicon Valley? A Case for Mechanism Design](https://www.oreilly.com/radar/what-happened-to-silicon-valley/) ⭐️ 7.0/10

O&\#x27;Reilly Radar published an essay arguing that Silicon Valley&\#x27;s incentives, corporate scale, and shareholder-value focus have reshaped technology, and that mechanism design — reverse game theory — offers a way to redesign the system around human flourishing. The piece traces how ZIRP-era cheap money and AI-driven growth turned venture culture toward enormous, profit-maximizing corporations. The argument matters because it reframes AI strategy and corporate governance as design problems rather than purely technical ones, suggesting that the goal society optimizes for can be deliberately chosen. It also bears on policy debates in California and beyond, where regulators are trying to balance AI oversight against the interests of the industry they regulate. The framing relies on mechanism design as taught by Nobel laureates such as Eric Maskin, who notes the theory applies to environmental policy, electoral systems, and financial markets. The article also connects to documented concerns that governance focused on maximizing shareholder value can incentivize harmful corporate behavior when enforcement is weak and penalties are low.

hackernews · Hacker News \(热门\) · Nov 22, 19:20 · [Discussion](https://news.ycombinator.com/item?id=50602947)

**Background**: Mechanism design is the study of how rules and institutions can be deliberately constructed so that self-interested participants produce desirable outcomes; as Maskin puts it, it is reverse game theory, asking not just what game is being played but what game ought to be played. It has long applications in market design, auction rules, and voting theory. Meanwhile, the shareholder value model reshaped corporate America in the 1980s and 1990s by tying executive compensation to stock price, and Silicon Valley&\#x27;s culture shifted as ZIRP-era cheap money let startups and incumbents grow to unprecedented scale.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanism_design">Mechanism design - Wikipedia</a></li>
<li><a href="https://www.ubs.com/global/en/our-firm/what-we-do/our-brand/nobel-perspectives/laureates/eric-maskin.html">Eric Maskin: Mechanism Design Theory | UBS Global</a></li>
<li><a href="https://phys.org/news/2025-09-good-corporate-incentives-bad-behavior.html">When &#x27;good&#x27; corporate governance creates incentives for bad behavior</a></li>

</ul>
</details>

**Discussion**: Commenters largely praised the article&\#x27;s mechanism-design framing, with one reader calling it a core topic of the era and agreeing that society should decide what to optimize for collectively. Others emphasized proximate causes such as ZIRP-era money enabling grotesque corporate scale, and questioned whether markets will now punish reckless AI spending, while one commenter criticized the shift from Wall Street yuppies to &quot;VC influencers&quot; and the perceived thinning of integrity in the Valley.

**Tags**: `#Silicon Valley`, `#AI Strategy`, `#Mechanism Design`, `#Corporate Incentives`, `#Technology Policy`

---

<a id="item-6"></a>
## [Show HN: A Game Where Players Become LLM Subagents](https://github.com/gulivan/worker755) ⭐️ 7.0/10

The open-source project worker755 presents an interactive game in which players act as an LLM subagent, receiving instructions from a managing agent while carrying out computer tasks. It turns agent delegation and command execution into a playful simulation and gained 261 points and 59 comments on Hacker News. The project provides an accessible way to experience the workflow of hierarchical multi-agent systems, where a coordinator delegates work to subordinate agents. Its reception shows strong interest in combining LLM agents with interactive fiction while also highlighting practical concerns such as local-model support. Gameplay involves responding to a director while executing shell-style commands, including humorous destructive commands such as rm -rf. One commenter observed that the manager often supplied exact commands rather than allowing independent solutions, and another noted that local LLM support did not appear to be available.

hackernews · Hacker News \(热门\) · Nov 22, 13:56 · [Discussion](https://news.ycombinator.com/item?id=50599762)

**Background**: An LLM subagent is a subordinate model instance given a narrower role within a larger agent workflow. In hierarchical multi-agent architectures, a primary orchestrator delegates tasks to specialized subagents that may perform reasoning, tool use, execution, or validation. worker755 gamifies this general pattern by making the human occupy the subagent position and act on commands issued by a managing agent.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/agents/architecture/multi-agent-orchestrator-sub-agent">Orchestrator and subagent multi-agent patterns | Microsoft Learn</a></li>
<li><a href="https://martinuke0.github.io/posts/subagents/">Sub-Agents in LLM Systems : Architecture, Execution Model ...</a></li>
<li><a href="https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture">Choosing the Right Multi-Agent Architecture - langchain.com</a></li>

</ul>
</details>

**Discussion**: Commenters generally found the game fun and humorous, particularly when testing dangerous shell commands and observing the director&\#x27;s reactions. Practical criticisms included the manager revealing exact solutions and the apparent absence of local LLM support, while the thread offered limited deeper analysis of the underlying agent architecture.

**Tags**: `#LLM agents`, `#Multi-agent systems`, `#Interactive fiction`, `#Open source`, `#Developer tools`

---

<a id="item-7"></a>
## [Japanese Automakers Standardize Parts to Cut Costs](https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/) ⭐️ 7.0/10

Toyota, Nissan, Honda, and other major Japanese automakers are pursuing greater standardization of vehicle components to reduce costs and improve competitiveness against Chinese manufacturers. The effort includes suppliers and broader supply-chain efficiencies, although the supplied material does not specify particular components or implementation dates. Sharing components can reduce development, procurement, and production costs across different vehicle models, helping Japanese automakers compete on price with efficient Chinese manufacturers. It may also require automakers and suppliers to coordinate more closely, potentially affecting parts suppliers and vehicle availability in global markets. Platform standardization generally means using common architectures and major components across multiple models, including engines, transmissions, and chassis in some cases. The available details do not establish which parts will be standardized, how much savings are expected, or whether all seven Japanese automakers named in the discussion are formally participating in the same program.

hackernews · Hacker News \(热门\) · Nov 22, 04:04 · [Discussion](https://news.ycombinator.com/item?id=50596133)

**Background**: A vehicle platform is a shared set of design, engineering, production, and major components used to support outwardly different models. Automakers use platform sharing to reduce development costs by limiting the number of distinct parts and architectures they must design and manufacture. Search results also describe broader cost-cutting efforts among Japanese automakers as competition from Chinese manufacturers intensifies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Car_platform">Car platform - Wikipedia</a></li>
<li><a href="https://www.nexdigm.com/market-research/insights/blog/modular-automotive-platform-analysis/">Modular Platform Analysis, Automotive Platform Strategy ...</a></li>
<li><a href="https://www.globalautoinsight.com/news/european-and-japanese-oems-losing-ground-to-china-cost-challenges">European and Japanese OEMs Losing Ground to China</a></li>

</ul>
</details>

**Discussion**: Commenters generally view parts standardization as a necessary response to Chinese automakers’ cost advantage, while some argue that the headline understates a trend affecting all major manufacturers. Comparisons were drawn to GM and Ford’s cooperation on a six-speed automatic transmission since 2002, although the shared clutch and gearing did not eliminate differences in solenoids and electronics; other comments questioned affordability and suggested the initiative could support Nissan’s financial position.

**Tags**: `#automotive-industry`, `#manufacturing`, `#supply-chain`, `#cost-reduction`, `#competition`

---

<a id="item-8"></a>
## [A Better Vocabulary for Software Testing](https://alperenkeles.com/posts/vocab-for-testing/) ⭐️ 7.0/10

The article proposes a richer testing vocabulary and a five-axis taxonomy for distinguishing what software tests examine and which quality concerns they address. It aims to replace ambiguous labels with more precise terms that teams can use to align testing scope, terminology, and expectations. Shared terminology helps engineers, reviewers, product stakeholders, and automated systems describe test intent consistently. More precise classification can improve test planning, reveal coverage gaps, and reduce disputes caused by labels such as unit, integration, functional, and non-functional testing. The proposed framework distinguishes five dimensions of testing concerns rather than relying only on the familiar model of functional versus non-functional properties and unit versus integration levels. Community participants suggested concrete semantic assertion names, such as an approximate-equality assertion with relative-error reporting, so failures can communicate both intent and remediation guidance.

hackernews · Hacker News \(热门\) · Nov 21, 22:15 · [Discussion](https://news.ycombinator.com/item?id=50594182)

**Background**: Software testing taxonomy attempts to organize tests according to what they cover, such as business behavior, performance, resilience, or robustness. Prior frameworks also distinguish test levels such as unit, integration, and system testing, but boundaries can become disputed when teams use the same labels for different concerns. CMU&\#x27;s software engineering institute has previously explored taxonomies as a way to assess testing expertise and plan more complete test programs.

<details><summary>References</summary>
<ul>
<li><a href="https://sei.cmu.edu/blog/a-taxonomy-of-testing/">A Taxonomy of Testing | CMU Software Engineering Institute</a></li>
<li><a href="https://ewh.ieee.org/r2/southern_nj/BarbacciOct03.pdf">Software Quality Attributes and</a></li>

</ul>
</details>

**Discussion**: Most commenters welcomed the proposed shared vocabulary and praised its ability to clarify distinct testing concerns. Others questioned whether the five-axis taxonomy adds enough practical value over the classic two-dimensional model, while suggesting that strongly typed languages can eliminate some invalid-input cases before runtime and simplify the unit-integration boundary.

**Tags**: `#software-testing`, `#testing-vocabulary`, `#quality-engineering`, `#software-architecture`, `#developer-tools`

---

<a id="item-9"></a>
## [Why Useless Knowledge Can Prove Profoundly Useful](https://www.ias.edu/sites/default/files/library/UsefulnessHarpers.pdf) ⭐️ 7.0/10

Harvey Harpers&\#x27;s 1939 essay argues that pursuing knowledge without an immediate practical application can generate major scientific and social benefits over time. The item resurfaced this historical argument as a concise case for supporting curiosity-driven basic research. The essay remains relevant to debates over how governments, universities, and funders should allocate money when basic research has uncertain or delayed returns. It challenges the assumption that research funding must promise immediate commercial or practical results. The central distinction is between immediate usefulness and longer-term value: apparently useless inquiry may create unexpected knowledge that becomes transformative in a different context. The available item provides only a summary and a link to comments, so it does not substantiate further technical claims or specific historical examples.

rss · Hacker News \(热门\) · Nov 22, 22:10

**Background**: Basic research seeks to expand knowledge rather than solve an immediate operational problem, and its practical benefits can emerge only after years or through applications not foreseen at the outset. Harpers&\#x27;s essay belongs to a broader historical defense of investigating questions whose value cannot yet be demonstrated.

**Tags**: `#research-policy`, `#basic-research`, `#history-of-science`, `#scientific-funding`, `#knowledge`

---

<a id="item-10"></a>
## [Localcode Brings One-Command Agentic Coding to macOS](https://github.com/mjwsolo/localcode) ⭐️ 7.0/10

Localcode is an open-source project for running agentic coding workflows locally on a Mac with a single command. The supplied item does not provide a release date, version, model support details, or other substantive feature information. The project could lower the setup barrier to local AI-assisted development while giving macOS users an open-source alternative to cloud-centered coding assistants. Its broader impact remains uncertain because the available description provides little evidence about capabilities, adoption, or reliability. Localcode is positioned around local-first operation, macOS support, and one-command setup, with source code hosted on GitHub. The provided material does not confirm whether it runs models fully on-device, which providers it supports, or what sandboxing and approval controls it provides.

rss · Hacker News \(热门\) · Nov 22, 22:18

**Background**: An AI coding agent can read project files, propose or make code changes, and execute development commands rather than merely returning a chat response. Local coding-agent projects increasingly focus on running models through local runtimes or connecting agents to local, open-weight models. Related tools such as Aider, Continue, OpenCode, and NanoTeams illustrate a broader ecosystem centered on open source, local-first development, though the search results do not establish Localcode&\#x27;s exact architecture or feature parity.

<details><summary>References</summary>
<ul>
<li><a href="https://reporank.net/en/repo/jmstajim-nanoteams.html">NanoTeams: Local - First AI Coding Agent for macOS - Open Source...</a></li>
<li><a href="https://github.com/baseguard/hangar">GitHub - baseguard/hangar: Run AI coding agents in a macOS , Linux...</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#open source`, `#macOS`, `#developer tools`, `#local-first`

---

<a id="item-11"></a>
## [Two Million AI Canaries Expose Widespread Secret Leakage](https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/) ⭐️ 7.0/10

A security researcher sent nearly two million AI prompts containing unique, trackable canary tokens to AI providers and detected cases where user secrets were exposed. The testing also uncovered prompt theft and providers apparently ignoring Zero Data Retention or no-data-collection settings. The findings suggest that privacy assurances offered by AI providers may not reliably survive across the AI software supply chain. Applications, developers, and users who place secrets in prompts could therefore face unexpected disclosure through provider workflows, logs, outputs, or downstream systems. The researcher used unique, trackable secrets embedded in prompts as canaries, allowing leakage to be identified without relying only on provider disclosures. Dragos reports three provider breaches, prompt theft, and instances in which Zero Data Retention settings were ignored, though the available material does not provide a complete methodology or impact breakdown.

rss · Lobsters \(技术社区\) · Nov 22, 02:03

**Background**: Canary tokens are deliberately embedded, unique markers that let researchers determine whether a specific artifact or piece of data reaches an unauthorized destination. In AI systems, prompts may pass among applications, model providers, plugins, logging services, and other downstream components, creating a supply chain in which data can be exposed even when an individual service appears secure. Zero Data Retention, commonly abbreviated ZDR, indicates that submitted data should not be stored, but the reported findings suggest that such contractual or technical controls may not always be enforced.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens">AI Supply Chain Security: What Canary Tokens Found | Dragos ...</a></li>
<li><a href="https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/">Researcher plants 2m canaries into the AI supply chain . A privacy ...</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#supply chain`, `#data privacy`, `#secret leakage`, `#canary tokens`

---

<a id="item-12"></a>
## [PostgreSQL Packaged as a Single Binary](https://progrium.xyz/articles/2026/single-binary-postgres) ⭐️ 7.0/10

The article presents a proof of concept named postgres-standalone, which embeds a complete PostgreSQL server into one executable that can run across platforms. The resulting miniPG project requires only a port and a data directory, while its underlying implementation reportedly used the Hyper9 compatibility layer to achieve near-native startup speeds. A single-file PostgreSQL distribution could simplify local development, testing, container workflows, and deployment by reducing the need to manage a separate database daemon and its surrounding installation files. The approach also illustrates how linking, compatibility layers, and build-time packaging can make a complex database easier to distribute. The stated result is a full PostgreSQL server and client in one executable, started with a port and a data directory. Development reportedly required three attempts to embed PostgreSQL, with the successful approach using Hyper9 to approach native startup performance; the available search results do not establish production readiness, supported platforms, or binary size.

rss · Lobsters \(技术社区\) · Nov 21, 19:32

**Background**: PostgreSQL is normally installed as multiple server and client executables plus supporting libraries, shared files, and configuration, although operating-system packages are available for many common platforms. Binary embedding is already used in some Java and Rust tooling, typically through configurable PostgreSQL distributions. The new effort differs by packaging the server directly into one executable for simpler operation and distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://progrium.xyz/articles/2026/single-binary-postgres">How I Got Postgres into a Single Binary · progrium</a></li>
<li><a href="https://news.lavx.hu/article/minipg-runs-real-postgres-from-a-single-executable">miniPG Runs Real Postgres From a Single Executable</a></li>
<li><a href="https://www.postgresql.org/docs/current/install-binaries.html">PostgreSQL: Documentation: 19: Chapter 16. Installation from ...</a></li>

</ul>
</details>

**Tags**: `#PostgreSQL`, `#binary packaging`, `#deployment`, `#databases`, `#systems engineering`

---

<a id="item-13"></a>
## [Microsoft 365 Outage Post-Incident Report](https://tianyin.github.io/misc/pir_microsoft_365_11-12-2026.pdf) ⭐️ 7.0/10

A post-incident report examines the causes and lessons of a significant Microsoft 365 outage affecting services such as Outlook. Search results attribute the incident to three interacting failures involving networking gateway servers, response handling, and cloud fabric. The outage demonstrated how failures in shared infrastructure can cascade across identity, collaboration, and communications services, disrupting organizations that depend on Microsoft 365. The report is operationally valuable for improving redundancy, health monitoring, and incident response in large distributed systems. Microsoft&\#x27;s root-cause analysis reportedly identified a previously undetected defect that could leave networking gateway servers unhealthy, alongside response and cloud fabric failures. Engineers isolated affected server groups, applied fixes, restarted them, and returned them to service gradually, while final review details were expected to clarify why redundancy and recovery systems did not contain the incident.

rss · Lobsters \(技术社区\) · Nov 21, 12:22

**Background**: Microsoft 365 is a collection of cloud productivity and communications services, including Outlook and related identity and collaboration capabilities. Such systems are distributed and highly redundant, but shared gateways and control layers can become common failure points. A post-incident review documents the timeline, causal chain, recovery process, and corrective actions so organizations can learn from major disruptions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Microsoft_outage">2026 Microsoft outage - Wikipedia</a></li>
<li><a href="https://windowsreport.com/microsoft-explains-root-cause-of-massive-outlook-and-exchange-outage-reveals-three-failures-behind-global-meltdown/">Microsoft Explains Root Cause of Massive Outlook and Exchange ...</a></li>
<li><a href="https://controlplane.com/blog/post/microsoft-365-outage-november-2026-cause">What Caused the Microsoft 365 Outage of November 12, 2026</a></li>

</ul>
</details>

**Tags**: `#Microsoft 365`, `#service reliability`, `#incident analysis`, `#distributed systems`, `#postmortem`

---

<a id="item-14"></a>
## [GhostScript Upload2Shell Vulnerability Enables Remote Code Execution](https://pwn.ai/upload2shell/research.html) ⭐️ 7.0/10

Researchers at pwn.ai disclosed CVE-2026-125396, nicknamed “Upload2Shell,” a GhostScript vulnerability that allows crafted files to escape the -dSAFER sandbox and execute commands on the server. The research page provides a central reference for the vulnerability and additional case studies and proof-of-concept material. GhostScript is widely used behind document conversion, preview, printing, thumbnail generation, and upload workflows, so a crafted file may trigger command execution even when users do not interact directly with GhostScript. The vulnerability therefore has broad implications for applications that process untrusted PostScript or PDF-related content. The flaw targets GhostScript versions earlier than 10.08.0, according to the cPanel advisory, and involves escaping the -dSAFER sandbox intended to block privileged operations such as arbitrary file writes and shell-command execution. Security researchers expect additional vulnerable software paths to emerge through uploads, thumbnails, print jobs, and document imports.

rss · Lobsters \(技术社区\) · Nov 22, 00:52

**Background**: GhostScript is a document-processing engine that interprets PostScript and PDF workflows used by many servers and desktop applications. Its -dSAFER mode is a defense-in-depth sandbox designed to stop malicious documents from writing files or invoking sensitive system operations. Upload2Shell demonstrates that crafted documents can potentially defeat this protection when GhostScript processes untrusted input.

<details><summary>References</summary>
<ul>
<li><a href="https://pwn.ai/upload2shell">Upload2Shell · CVE - 2026 - 125396 · pwn.ai research</a></li>
<li><a href="https://support.cpanel.net/hc/en-us/articles/45216747700503-Security-CVE-2026-125396-Ghostscript-Upload2Shell">Security: CVE-2026-125396 - Ghostscript - Upload2Shell – cPanel</a></li>
<li><a href="https://www.valtersit.com/cve/CVE-2026-125396">CVE - 2026 - 125396 | Artifex | Valters IT Hub</a></li>

</ul>
</details>

**Tags**: `#GhostScript`, `#CVE-2026-125396`, `#vulnerability`, `#file processing`, `#security research`

---

<a id="item-15"></a>
## [Muru Brings Rust-Powered Production Tooling to Python](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

Graham Dumpleton, creator of mod\_wsgi, introduced Muru, an AI-assisted Rust server for running both ASGI and WSGI Python applications in development and production. A detailed series of posts published from November 4–22, 2026 covers its workers, release model, container and Kubernetes integration, scaling, tracing, and use of lazy imports. Muru could simplify Python deployment by consolidating functions commonly spread across a reverse proxy, application server, process supervisor, and deployment tooling. Its Rust implementation and support for both application models may appeal to teams seeking modern operational features without abandoning existing Python codebases. Muru&\#x27;s documentation says its edge layer handles HTTP/1.1, HTTP/2, TLS, virtual hosts, static files, uploads, compression, and errors directly, leaving worker threads more time for Python work. The project is still being presented through a development diary, so the announcement demonstrates intended architecture and tooling rather than broad production adoption; Dumpleton also emphasizes that human review remains central to deciding whether AI-generated work is good enough.

rss · Simon Willison \(AI 跨行业洞察\) · Nov 21, 23:56

**Background**: WSGI is Python&\#x27;s older synchronous web-application interface, while ASGI is an asynchronous interface designed to handle concurrent requests. mod\_wsgi, created by Graham Dumpleton 20 years ago, embeds Python applications in an Apache HTTP Server process. Muru is his attempt to revisit production Python serving with a modern Rust-based architecture and unified ASGI and WSGI support.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Nov/21/muru/">Muru - simonwillison.net</a></li>
<li><a href="https://docs.muruhq.dev/">Muru ¶</a></li>
<li><a href="https://www.theprotec.com/blog/muru-rust-server-python-app-deployment/">How the Muru Rust server Could Rethink Python App Deployment</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Rust`, `#ASGI`, `#WSGI`, `#Web Servers`

---

<a id="item-16"></a>
## [Signal Restricts Mobile Screenshots Against AI Surveillance](https://techcrunch.com/2026/11/21/signal-restricts-mobile-screenshots-as-it-confronts-existential-threat-of-ai-surveillance/) ⭐️ 7.0/10

Signal is limiting users’ ability to take screenshots within its Android and iOS applications. The restriction is part of the messaging platform’s effort to prevent private conversations from being exposed to AI-assisted surveillance. The change reflects growing concern that operating-system AI assistants and other screen-reading tools can collect sensitive content despite Signal’s encryption. It highlights a broader limitation of encrypted messaging: once data appears on a compromised endpoint, application-level protections cannot fully control how it is accessed. Signal previously documented using Screen Security to hide message previews in the Android app switcher, but its newer protections are aimed at blocking AI assistants such as Google Gemini and Siri from reading on-screen conversations. The available material does not specify which screenshot operations are blocked, which app versions are affected, or whether every Android and iOS device receives identical restrictions.

rss · TechCrunch AI · Nov 21, 21:37

**Background**: Screen Security can prevent Signal content from appearing in the phone’s app switcher, reducing one route through which sensitive messages become visible. Signal says increasingly capable AI assistants can read whatever is displayed on screen and may make that data available to agentic systems, undermining the app’s ability to independently guarantee privacy. Blocking screenshots is therefore an endpoint-protection measure intended to keep private conversations out of AI-readable screen content.

<details><summary>References</summary>
<ul>
<li><a href="https://support.signal.org/hc/en-us/articles/11338514641306-Screen-security-blocking-Google-Gemini-and-Siri-AI">Screen security: blocking Google Gemini and Siri AI – Signal ...</a></li>
<li><a href="https://support.signal.org/hc/en-us/articles/360043469312-Screen-Security">Screen Security - Signal Support</a></li>
<li><a href="https://signal.org/blog/protecting-your-privacy/">Signal is Serious About Protecting Your Privacy</a></li>

</ul>
</details>

**Tags**: `#Signal`, `#Mobile Security`, `#Privacy`, `#AI Surveillance`, `#Encrypted Messaging`

---

<a id="item-17"></a>
## [Race Realism Misuses Genetics, Article Argues](https://arstechnica.com/science/2026/11/race-realism-isnt-realistic-and-it-isnt-good-science/) ⭐️ 7.0/10

The article argues that modern genetics does not support claims that intelligence differences are innate and biologically tied to race. It characterizes such claims as scientifically unrealistic and challenges the scientific framing used by race-realist advocates. The dispute over genetic causes of cognitive differences affects how researchers, technology companies, and policymakers interpret group-level disparities. Misusing population genetics could legitimize discriminatory practices or produce biased AI systems and fairness policies. Human biological variation often follows geographic clines rather than sharp racial boundaries, while genetic ancestry and socially defined race are not interchangeable categories. Estimates that cognitive-test performance is partly heritable describe variance within populations and do not, by themselves, establish innate differences between racial groups or identify genetic causes of group gaps.

rss · Ars Technica · Nov 21, 12:01

**Background**: A cline is a measurable biological gradient across geography; skin pigmentation is a commonly cited example of continuous variation without clearly bounded racial categories. In behavioral genetics, heritability quantifies how much variation within a given population and environment is associated with genetic differences, not the causes of differences between populations. Genetic ancestry can inform human variation research, but it does not make socially constructed racial classifications biologically discrete or establish innate group-level intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://www.encyclopedia.com/social-sciences/encyclopedias-almanacs-transcripts-and-maps/clines-and-continuous-variation">Clines and Continuous Variation - Encyclopedia.com Clinal Distribution (Gradual Variation in Biological ... 6.3: Clinal Variation - Social Sci LibreTexts Modern Human Variation Models - theoptionalist.com 13.3: Human Variation in Biological Anthropology Today Clinal Variation: Why There Are No Biological Races</a></li>
<li><a href="https://quillette.com/2023/01/08/more-than-just-a-social-construct/">More Than Just a Social Construct</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2889158/">The heritability of general cognitive ability increases ...</a></li>

</ul>
</details>

**Tags**: `#race and genetics`, `#intelligence research`, `#scientific validity`, `#AI bias`, `#algorithmic fairness`

---

<a id="item-18"></a>
## [U.S. Banks Restrict Third-Party AI Agents](https://www.wired.com/story/banks-are-cracking-down-on-ai-agents/) ⭐️ 7.0/10

Major U.S. banks are blocking third-party AI agents from accessing customer accounts and disclaiming responsibility for costly mistakes made by those bots. The restrictions target agents that log in using customer-shared credentials. The measures could materially limit consumer agentic AI deployments in financial services unless banks offer secure agent access or regulated alternatives. They also shift liability toward users and raise difficult authentication and control questions for banks, fintechs, and agent developers. Reportedly, banks detected unvetted third-party agents accessing customer accounts with shared credentials, prompting access restrictions. The cutoff is an operational and contractual control rather than a general prohibition on banks deploying their own AI systems.

rss · Wired · Nov 22, 11:00

**Background**: AI agents can perform online banking tasks by operating browsers or APIs on a user&\#x27;s behalf. Because such agents may hold or reuse customer credentials, banks face challenges in distinguishing legitimate automation from unauthorized access and determining who bears responsibility when an agent causes financial harm.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bankingnewsai.com/ai-incidents/us-banks-2026-unauthorized-third-party-ai-agents-in-accounts">Unvetted AI agents found in US bank customer accounts ; Morgan...</a></li>
<li><a href="https://pondero.ai/news/2026-10-24-ai-agents-bank-account-gap/">Report: unvetted AI agents still reach some US bank accounts after...</a></li>
<li><a href="https://blog.traversaal.ai/agentic-ai-banking-insurance-production-vs-pilots/">Agentic AI in Banking vs. Insurance: Why Banking Is Scaling in...</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Financial Services`, `#Authentication`, `#AI Security`, `#Regulation`

---

<a id="item-19"></a>
## [Life’s Chemical Reactions Persisted in Sterilized Soil for Six Years](https://www.wired.com/story/scientists-tried-to-kill-this-dirt-but-it-wouldnt-die/) ⭐️ 7.0/10

Researchers found that biologically important chemical reactions continued in sterilized soil over a six-year period. The result suggests that soil chemistry alone may sustain some reactions relevant to the emergence of life. The finding offers new evidence for how prebiotic chemistry could have operated on early Earth without living organisms. It may help researchers identify environmental conditions that supported chemical pathways potentially involved in abiogenesis. The key observation was persistence, not the production of life: biologically important reactions remained detectable for six years in sterilized soil. The supplied material does not specify which reactions were measured, the sterilization method, the soil conditions, or whether the experiment demonstrated a complete pathway toward living systems.

rss · Wired · Nov 22, 10:30

**Background**: Prebiotic chemistry studies how organic compounds formed and self-organized before life existed, providing a framework for understanding abiogenesis. Abiogenesis is the natural process by which life arises from nonliving matter through chemical steps. The soil experiment tests whether environments lacking active organisms can nevertheless sustain chemically relevant reactions over long periods.

<details><summary>References</summary>
<ul>
<li><a href="https://biologyinsights.com/what-is-abiogenesis-the-scientific-origin-of-life/">What Is Abiogenesis? The Scientific Origin of Life</a></li>
<li><a href="https://en.wikipedia.org/wiki/Abiogenesis">Abiogenesis - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Origin of Life`, `#Prebiotic Chemistry`, `#Soil Microbiology`, `#Abiogenesis`, `#Scientific Research`

---

<a id="item-20"></a>
## [AI Accelerates Exploits Beyond the Patch Window](https://www.wired.com/story/brace-yourself-for-years-of-outage-chaos/) ⭐️ 7.0/10

AI-enabled attackers are discovering vulnerabilities and developing working exploits faster than many organizations can deploy patches. This shortens the interval between disclosure and exploitation, increasing the risk that widely used internet services will suffer prolonged outages. The emerging exploit-before-patch gap makes conventional patch management less effective at containing fast-moving threats. Organizations need faster vulnerability triage, remediation, and service-resilience measures, while attackers gain a lower technical barrier to turning newly found flaws into operational attacks. Google Cloud reports that adversaries are beginning to use agentic AI for discrete offensive tasks, including developing novel exploits and supporting human operators. The available results indicate these systems can operate at machine speed across multi-stage intrusions, but they do not quantify a universal outage duration or the precise AI-driven reduction in patch time.

rss · Wired · Nov 21, 13:00

**Background**: A patch window is the period between a vulnerability becoming known or exploitable and the affected system receiving a fix. Agentic AI refers to systems that can plan and carry out multi-step tasks with limited human direction, making exploit development more scalable and potentially faster. Cloud Security Alliance describes the exploit-before-patch gap as the problem of attackers producing usable exploits before defenders finish patching.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks">ARTEX and Friends: Enter Agentic Offensive... | Google Cloud Blog</a></li>
<li><a href="https://www.youtube.com/watch?v=K0DRjjpRwqw">Agentic AI Threat Activity in Cyber Operations - YouTube</a></li>

</ul>
</details>

**Tags**: `#AI cybersecurity`, `#vulnerability patching`, `#internet outages`, `#exploit development`, `#cybersecurity`

---

<a id="item-21"></a>
## [Typed Slot Memory Preserves Facts During Context Compaction](https://dev.to/yuya_ai_lab/your-agent-forgot-the-order-number-compacting-context-without-losing-facts-pure-python-53lb) ⭐️ 7.0/10

The article introduces a dependency-free, pure-Python typed slot-memory system for fitting long agent conversations into limited token budgets. Across 400 seeded synthetic transcripts, it reports nearly 100% fact recall, with 95.8% of sessions fully answerable at a 10% budget using 148 of 1,557 estimated tokens. The work addresses a common production failure in which agents silently discard old but essential details, such as order numbers, deadlines, budgets, and constraints, merely because they occurred early in a conversation. Typed slot memory offers a more targeted and auditable alternative to keeping recent turns or relying on nondeterministic model-generated summaries. The offline corpus contains 400 seeded support conversations of 30–70 turns, with three answer-critical facts per session and stale order identifiers introduced in 35% of sessions. Evaluation measures whether exact facts remain in the prompt, not whether a model answers correctly, and token counts come from a regex tokenizer rather than a BPE tokenizer; the study therefore does not establish real-world model accuracy.

rss · Dev.to · Nov 22, 23:47

**Background**: An LLM agent has a finite context window that may hold conversation history, retrieved knowledge, system instructions, and tool results. When that space fills, common policies either keep the newest turns, extract salient passages, summarize old content, or store structured facts externally. Slot memory belongs to the structured-fact category: selected values are assigned typed slots, updated when corrections occur, and rendered into the prompt when space is constrained.

<details><summary>References</summary>
<ul>
<li><a href="https://llmengg.com/context-window-management-multi-agent/">Context Window Management for Multi- Agent AI — Workshop April...</a></li>
<li><a href="https://aiagentmemory.org/articles/llm-context-window-overflow/">LLM Context Window Overflow: Strategies and Solutions for</a></li>
<li><a href="https://genmind.ch/posts/Your-LLM-Has-Amnesia-A-Production-Guide-to-Memory-That-Actually-Works/">Your LLM Has Amnesia: A Production Guide to Memory That Actually...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#context management`, `#memory systems`, `#prompt compression`, `#Python`

---

<a id="item-22"></a>
## [AI Ported One Python Function to Rust for 78× Speedup](https://dev.to/frankchu/78x-faster-my-python-dedupe-5-rewritten-in-rust-27d6) ⭐️ 7.0/10

The fast-anything tool identified a performance-critical Python function, recorded its real invocations, generated a Rust port, and validated equivalent outputs across 34 test cases before enabling it. In the author&\#x27;s fuzzy-deduplication example, changing one 48-line function reduced runtime from 10.06 seconds to 129 milliseconds while leaving the rest of the application unchanged. The experiment illustrates a selective optimization strategy that can avoid rewriting an entire Python application when only a small computational bottleneck matters. If reproducible on production workloads, this approach could shorten performance-engineering cycles, though the tool&\#x27;s maturity and general reliability remain uncertain. The rewritten function implements Levenshtein-distance computation within a deliberately naive quadratic pairwise loop over 700 names, making it an ideal CPU-bound test case. The reported 78× result is a single author&\#x27;s benchmark rather than an independent evaluation, and the supplied article excerpt does not establish how the Rust function is integrated with Python.

rss · Dev.to · Nov 22, 23:41

**Background**: Levenshtein distance measures the minimum number of single-character insertions, deletions, and substitutions needed to transform one string into another, making it useful for identifying names that differ by typos. Comparing every pair with a quadratic implementation can become expensive as the dataset grows. Incremental Python-to-Rust porting offers an alternative to full rewrites, although cross-language integration and behavioral equivalence must be handled carefully.

<details><summary>References</summary>
<ul>
<li><a href="https://tutorials.tektite.studio/fuzzy-matching/fuzzy-string-matching-algorithms/">Fuzzy String Matching Algorithms Explained</a></li>
<li><a href="https://www.datablist.com/learn/data-cleaning/fuzzy-matching-levenshtein-distance">What is Levenshtein distance for fuzzy matching? - Datablist</a></li>
<li><a href="https://international-bsf.org/courses/certificate-in-open-banking/lessons/lesson-9-2-fuzzy-matching-and-merchant-deduplication-the-levenshtein-jaro-winkler-and-soundex-algorithm-suite/">LESSON 9.2: FUZZY MATCHING AND MERCHANT DEDUPLICATION — The ...</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Rust`, `#performance-optimization`, `#AI-assisted-development`, `#testing`

---

<a id="item-23"></a>
## [Beginner’s Guide to Local AI with Inkling, Qwen, and Unsloth](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth) ⭐️ 6.0/10

The article presents a beginner-oriented workflow for running and fine-tuning local language models with Inkling, Qwen, and Unsloth. It also examines the hardware constraints, VRAM requirements, AMD NPU support, and practical deployments involved in local AI. By consolidating setup guidance and realistic hardware expectations, the guide can make local AI more accessible to developers and enthusiasts. It also highlights the continuing gap between consumer machines and frontier cloud models, as well as the role of efficient fine-tuning and accelerator support in narrowing that gap. The discussion centers on model quantization, VRAM calculations, multi-GPU setups, and AMD NPU support; one commenter proposed replacing a fixed 1 GB graphics-memory overhead with a configurable baseline. A reported Ryzen AI 350 system ran Qwen3.5-9B at about 12 tokens per second, but the commenter judged its output unreliable and not comparable to frontier models.

hackernews · Hacker News \(热门\) · Nov 22, 21:01 · [Discussion](https://news.ycombinator.com/item?id=50603845)

**Background**: Local AI refers to running language models on a user’s own computer rather than sending requests to a remote API. Qwen is Alibaba Cloud’s family of open-weight models, while Unsloth is an open-source framework for fine-tuning and post-training them. Inkling is described in the search material as an Apache 2.0-licensed, open-weights sparse mixture-of-experts model from Thinking Machines Lab that accepts text, image, and audio input.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Inkling_%28large_language_model%29">Inkling (large language model) - Wikipedia</a></li>
<li><a href="https://qwen.ai/home">Qwen</a></li>
<li><a href="https://unsloth.ai/docs/get-started/fine-tuning-llms-guide">Fine-tuning LLMs Guide | Unsloth Documentation</a></li>

</ul>
</details>

**Discussion**: Commenters described local AI as an early “plasma TV phase” and questioned whether current hardware is practical for ordinary consumers, while sharing projects that run local models on macOS, BSD, and AMD systems. Enthusiasm for fully local audiobook narration and Qwen3.5-9B was tempered by concerns about VRAM, output reliability, and performance relative to frontier models; one commenter suggested a configurable VRAM baseline for the calculator.

**Tags**: `#local-ai`, `#Qwen`, `#Unsloth`, `#LLM-fine-tuning`, `#consumer-hardware`

---

<a id="item-24"></a>
## [Alliance Proposes Shared Protocol for Open Social Media](https://osw-alliance.net/en/) ⭐️ 6.0/10

The Open Social Web Alliance proposes a common communication protocol for interoperable, resilient social platforms intended to support democratic discourse. Its vision also includes portable identities and connections among independent services such as Mastodon, Mu, and Streamplace. A shared protocol could reduce dependence on closed social platforms and make it easier for users to move between services without losing posts, followers, or identities. It also seeks to challenge the business incentives of large platforms, which critics argue often profit more from engagement and conflict than from constructive public discourse. The alliance describes the Open Social Web as decentralized public-interest infrastructure based on open standards and interoperable protocols, supplementing projects such as Mastodon and Eurosky. However, the presentation has been criticized as vague and promotional, and the specific protocol design, governance model, and adoption path remain unclear in the supplied material.

hackernews · Hacker News \(热门\) · Nov 22, 15:24 · [Discussion](https://news.ycombinator.com/item?id=50600511)

**Background**: Interoperability allows users and services to exchange data and interact through shared interfaces rather than proprietary systems. Earlier efforts such as OpenSocial defined common application programming interfaces for social web applications, while many contemporary federated platforms use ActivityPub to connect independent servers. The alliance frames its proposal as an extension of this broader effort to create a decentralized, portable social web.

<details><summary>References</summary>
<ul>
<li><a href="https://osw-alliance.net/en/">Open Social Web Alliance – OSW-Alliance.net</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fediverse">Fediverse - Wikipedia</a></li>
<li><a href="https://www.theprotec.com/blog/europe-open-social-web-beyond-meta/">Can Europe Build an Open Social Web Beyond Meta’s Platforms?</a></li>

</ul>
</details>

**Discussion**: Commenters strongly doubted that a technical protocol could repair democratic discourse, arguing that political organizing and changes to economic incentives are more important. They also called the announcement overly fluffy and difficult to understand, while some expressed interest in platforms that resist bots, rate-limit participation, and avoid engagement-maximizing algorithms.

**Tags**: `#open-social-web`, `#protocols`, `#social-media`, `#interoperability`, `#online-democracy`

---

<a id="item-25"></a>
## [How BSD Escaped AT&amp;T&\#x27;s Unix Licensing](https://fosscomics.com/posts/16.%20BSD%20Unix%20Part%206%20-%20The%20Struggle%20for%20Freedom/) ⭐️ 6.0/10

This retrospective examines the legal and technical efforts that allowed BSD Unix to emerge as an independently licensed operating system rather than a derivative constrained by AT&amp;T&\#x27;s proprietary Unix license. It is a historical account rather than a new technical release. The story explains how BSD became one of the foundations of modern open-source operating systems and influenced later projects such as FreeBSD, OpenBSD, and NetBSD. It also illustrates how licensing disputes shaped software freedom and the broader Unix ecosystem. Early BSD releases incorporated AT&amp;T Unix source code and therefore had to follow AT&amp;T&\#x27;s restrictive license. The later separation was achieved through legal action, licensing changes, and technical replacement of AT&amp;T-derived components, enabling BSD to be distributed under an open-source license.

rss · Hacker News \(热门\) · Nov 22, 21:33

**Background**: The Berkeley Software Distribution began at the University of California, Berkeley, as an improved derivative of AT&amp;T Unix. AT&amp;T&\#x27;s source-code license initially prevented BSD from being distributed freely, but AT&amp;T&\#x27;s 1984 divestiture and subsequent legal disputes helped create room for an independently licensed BSD. The 1992 lawsuit by AT&amp;T and its 1994 settlement are commonly identified as important events in that conflict.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/History_of_the_Berkeley_Software_Distribution">History of the Berkeley Software Distribution - Wikipedia</a></li>
<li><a href="https://machaddr.substack.com/p/the-at-and-t-and-bsd-conflict-unix">The AT&amp;T and BSD Conflict: UNIX Wars - André Machado | Blog</a></li>

</ul>
</details>

**Tags**: `#BSD`, `#Unix`, `#Open Source History`, `#AT&amp;T Licensing`, `#Software Freedom`

---

<a id="item-26"></a>
## [Harvard Offers Graduate Course on AI Alignment and Safety](https://boazbk.github.io/mltheoryseminar/) ⭐️ 6.0/10

Harvard&\#x27;s COMPSCI 2881R, titled “AI Alignment and Safety,” is listed for Fall 2026 as a graduate course addressing technical and societal challenges in AI alignment and safety. Course materials are available through the linked GitHub Pages site. The course formalizes AI safety and alignment as subjects of graduate study within computer science, potentially training researchers and engineers to evaluate and address advanced AI risks. It also connects technical research with broader societal and governance questions. COMPSCI 2881R是一门研究生级别的研究研讨课，据课程相关反思文章介绍，学生需要复现重要的人工智能安全论文并开展原创研究。现有公告对作业、评分标准、授课教师和完整日程介绍很少，因此不能把这些材料视为一份完整课程大纲。

rss · Hacker News \(热门\) · Nov 22, 18:01

**Background**: AI alignment generally concerns whether advanced AI systems behave consistently with intended human values and instructions. AI safety is a broader field that also includes robustness, monitoring, capability control, and assessment of societal risks; this course examines both its technical and societal dimensions.

**Tags**: `#AI safety`, `#machine learning theory`, `#academic course`, `#AI alignment`

---

<a id="item-27"></a>
## [Common Misconceptions About ATProto](https://reiver.link/atproto/falsehoods-programmers-believe/) ⭐️ 6.0/10

The article identifies false assumptions that programmers commonly hold about the AT Protocol and explains how the system actually behaves. The available excerpt links to community discussion but does not expose the article’s specific claims. Correctly understanding ATProto’s architecture is important for developers building decentralized social applications. Misconceptions about data ordering, identity resolution, or event delivery could lead to faulty implementations and unreliable integrations. ATProto repositories are key-value mappings whose records are stored in key-sorted order using a Merkle Search Tree, while human-readable handles can be resolved through DIDs such as did:plc. These official specifications provide concrete details that programmers should check before drawing broader conclusions about the protocol.

rss · Lobsters \(技术社区\) · Nov 22, 16:37

**Background**: The AT Protocol is a set of open standards for decentralized publishing and the distribution of self-authenticating data, and it serves as the technical foundation of Bluesky. Its repository model uses deterministic, content-addressed structures, while its identity system separates user-friendly handles from DID-based records that identify hosting services and key material.

<details><summary>References</summary>
<ul>
<li><a href="https://atproto.com/specs/repository">Repository - AT Protocol</a></li>
<li><a href="https://atproto.com/guides/identity">Identity - AT Protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#ATProto`, `#Software Architecture`, `#Developer Education`, `#Distributed Systems`

---

<a id="item-28"></a>
## [Gliver Completes the Guix Desktop Environment](https://dustycloud.org/blog/gliver-completes-the-guix-desktop/) ⭐️ 6.0/10

Gliver has added the final components needed to turn GNU Guix into a complete desktop environment. The announcement describes this milestone as completing the Guix desktop stack. 完整的桌面环境让 Guix 在保留函数式包管理和可复现配置特性的同时，更适合日常使用。它可能吸引希望采用可复现、声明式桌面方案的普通用户和开发者。 The supplied article includes only a link to the discussion and provides no component list, version number, release date, or testing details. Consequently, the precise scope of the completion and any remaining limitations cannot be verified from the available material.

rss · Lobsters \(技术社区\) · Nov 22, 20:10

**Background**: GNU Guix is a functional package manager and system-management tool inspired by Nix, with package recipes and configuration written in Guile Scheme. It can operate as part of another GNU/Linux distribution or as the standalone Guix System. Gliver&\#x27;s work focuses on supplying the desktop layer needed to use that foundation as a full graphical workstation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GNU_Guix">GNU Guix - Wikipedia</a></li>
<li><a href="https://wiki.archlinux.org/title/Guix">Guix - ArchWiki</a></li>

</ul>
</details>

**Tags**: `#Guix`, `#GNU/Linux`, `#Functional Computing`, `#Desktop Environment`, `#Reproducible Builds`

---

<a id="item-29"></a>
## [NixOS Brought Up on Alibaba RISC-V Board](https://feyor.sh/blog/nixos-bringup-on-an-alibaba-riscv-board/) ⭐️ 6.0/10

A blog post documents the process of porting and booting NixOS on an Alibaba RISC-V development board. The published excerpt contains only a link to the discussion, so the specific board model, software version, and achieved functionality are not stated. The effort may contribute practical knowledge for extending NixOS hardware support and enabling the growing RISC-V software ecosystem. Its value is primarily technical and documentary, although the limited excerpt provides little evidence about the port&\#x27;s completeness or broader adoption. The available material identifies the target as an Alibaba RISC-V development board and links to a Lobsters discussion. NixOS documentation notes that riscv64-linux is not officially supported in the stable and unstable channels, making individual board ports an important part of enabling the architecture; however, no board revision, kernel configuration, bootloader, driver status, or test results are available here.

rss · Lobsters \(技术社区\) · Nov 22, 00:30

**Background**: NixOS is a Linux distribution built around the Nix package manager and declarative, reproducible system configuration. RISC-V is an open instruction-set architecture whose boards can differ substantially in peripherals, firmware, and required drivers, so bringing up a new board commonly involves adapting the bootloader, kernel, device tree, and hardware configuration. Existing community efforts also pursue NixOS on RISC-V through cross-compilation and board-specific support.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/robinfinkelmann/fml13v01-nixos">robinfinkelmann/fml13 v 01- nixos : NixOS for the DeepComputing RiscV ...</a></li>
<li><a href="https://nixos.wiki/wiki/NixOS_on_ARM">NixOS on ARM - NixOS Wiki</a></li>

</ul>
</details>

**Tags**: `#NixOS`, `#RISC-V`, `#Linux`, `#hardware-porting`, `#Alibaba`

---

<a id="item-30"></a>
## [Open-Source Calculator Plans City-Scale Radio Mesh Networks](https://meshcoveragecalculator.lalala.ing/) ⭐️ 6.0/10

A new open-source, local-first WASM calculator estimates radio-link placement and node counts for city-scale mesh networks. It combines FSPL and Delta-Bullington propagation models and is available with its source code. The tool could make early-stage community and Meshtastic network planning more accessible by providing a browser-based way to estimate coverage and infrastructure needs. It may help operators reduce unnecessary nodes and identify placements more likely to maintain viable links. The calculator uses free-space path loss, or FSPL, for basic signal-loss estimation and the Delta-Bullington model for irregular-terrain propagation; Delta-Bullington is fast and geographically continuous but can require accurate clutter data. The announcement provides no validation results, supported hardware inventory, precision figures, or detailed comparison with established planners.

rss · Lobsters \(技术社区\) · Nov 22, 18:17

**Background**: FSPL estimates radio attenuation with distance and frequency and is commonly used in wireless link budgets. Delta-Bullington extends basic propagation analysis to irregular terrain, while existing Meshtastic Site Planner software also offers terrain-based coverage mapping and adjustable radio parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://meshtastic.org/blog/meshtastic-site-planner-introduction/">Meshtastic Site Planner, an Open Source Tool to Optimize Your ...</a></li>
<li><a href="https://meshtastic.org/docs/software/site-planner/">Meshtastic Site Planner</a></li>

</ul>
</details>

**Tags**: `#mesh-networks`, `#radio-propagation`, `#network-planning`, `#WASM`, `#Meshtastic`

---

<a id="item-31"></a>
## [Advice for the Next 100 Rust GUIs](https://linebender.org/blog/next-100-guis/) ⭐️ 6.0/10

The Linebender blog published an article titled &quot;Advice for the next 100 Rust GUIs,&quot; a synthesis of hard-won guidance for building Rust-based graphical user interfaces. The post collects lessons drawn from practical experience across multiple Rust GUI projects and is paired with a discussion thread on Lobsters. Rust&\#x27;s GUI ecosystem has proliferated into many competing frameworks — egui, iced, Slint, Druid, Xilem, and others — each with its own architecture and tradeoffs, so shared guidance can help newcomers avoid repeating the same mistakes. For teams choosing a stack or designing their own toolkit, this kind of distilled advice is a useful complement to framework documentation and comparison guides. The available content is minimal — essentially a title, a link, and a pointer to the Lobsters comment thread — so the article&\#x27;s specific recommendations, technical depth, and level of originality could not be verified from the provided material. Readers should consult the post and its comments directly for the actual list of lessons.

rss · Lobsters \(技术社区\) · Nov 21, 23:10

**Background**: Rust GUI development spans two broad architectural families: immediate-mode UIs, which rebuild the widget tree every frame from application state, and retained-mode UIs, which keep a persistent widget tree and diff or patch it on change. Frameworks such as iced follow the Elm-style separation of state, messages, and view/update logic, while egui and Slint represent other approaches, and Xilem is an experimental reactive framework from Druid creator Raph Levien. Linebender is the group behind the winit and wgpu ecosystem, whose members have worked on several of these GUI efforts, which explains their interest in codifying cross-project lessons.

<details><summary>References</summary>
<ul>
<li><a href="https://rust.codeguides.io/desktop-gui/rust-gui-architecture-models/">Rust GUI Architecture Models - Rust SME Cookbook</a></li>
<li><a href="https://github.com/iced-rs/iced">GitHub - iced-rs/iced: A cross-platform GUI library for Rust , inspired by...</a></li>
<li><a href="https://gpui-starter.freeoxide.com/blog/rust-gui-frameworks-comparison-2026/">Rust GUI frameworks in 2026: the complete comparison guide</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#GUI`, `#Software Architecture`, `#Developer Tools`

---

<a id="item-32"></a>
## [Sutskever Proposes Measurable AI Development Speed Limits](https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/) ⭐️ 6.0/10

OpenAI chief scientist Ilya Sutskever argues that governing the pace of AI development will require a measurable framework comparable to speed limits. The core obstacle is agreeing on how to measure that development speed. A workable measurement framework could become a foundation for voluntary commitments or regulation of frontier AI development. It would also give policymakers and AI companies a more concrete way to discuss when capabilities are advancing too quickly for safeguards and oversight. The reported proposal is a speed-limit analogy rather than a fully specified policy, and the available excerpt does not identify the metrics, thresholds, enforcement mechanisms, or institutions involved. The central technical and governance challenge is establishing a measure that is meaningful, comparable, and resistant to gaming.

rss · TechCrunch AI · Nov 22, 21:14

**Background**: AI development speed limits are proposed as a way to regulate how rapidly AI systems improve before potentially outpacing human oversight. Existing measurement efforts focus on different goals: McKinsey’s framework assesses AI adoption, operations, and financial impact, while Anthropic’s reported three-metric framework tracks research and product-cycle pace. OpenAI’s 2023 governance discussion emphasized preparing for superintelligence, a term used for future systems dramatically more capable than current AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/from-promise-to-impact-how-companies-can-measure-and-realize-the-full-value-of-ai">The five-layer AI measurement framework | McKinsey</a></li>
<li><a href="https://ceoconnectmagazine.com/anthropic-development-metrics/">How Anthropic’s Three‑Metric Framework Can Guide AI Development ...</a></li>
<li><a href="https://pen-vape.com/tech-innovation/anthropic-ceo-amodei-wants-ai-speed-limits-before-self-improvement-outpaces-huma/">Anthropic CEO Amodei Wants AI Speed Limits Before... - Pen Vape</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#AI safety`, `#AI policy`, `#OpenAI`, `#Ilya Sutskever`

---

<a id="item-33"></a>
## [Nvidia’s Earnings and Leadership Crisis](https://techcrunch.com/2026/11/21/a-tale-of-two-nvidias/) ⭐️ 6.0/10

TechCrunch contrasts Nvidia’s latest earnings performance with prominent technology executives calling for co-founder Jensen Huang to return as CEO. The article examines the tension between strong financial results and the leadership upheaval surrounding Huang. Nvidia’s earnings demonstrate the commercial strength of its AI semiconductor business, while calls for Huang’s return highlight the importance of leadership continuity to investors and industry executives. Any resolution could influence Nvidia’s strategy, governance, and market confidence. Nvidia reported fiscal fourth-quarter 2025 revenue of $39.3 billion, up 78% year over year, and non-GAAP diluted earnings per share of $2.99, up 130%, alongside strong Blackwell demand. Separately, Huang said he would be willing to return after resigning, according to reports dated November 2026.

rss · TechCrunch AI · Nov 21, 21:07

**Background**: Nvidia is a semiconductor company whose growth has been closely tied to demand for data-center accelerators used in AI training and inference. Blackwell is its newer data-center GPU architecture, and Huang has served as the company’s founder and central strategic leader. The leadership question therefore concerns both corporate governance and the continuity of Nvidia’s AI-focused strategy.

<details><summary>References</summary>
<ul>
<li><a href="https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2025/">NVIDIA Corporation - NVIDIA Announces Financial Results for ...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/17/nvidia-jensen-huang-statement">Jensen Huang says he would be ‘honored’ to return to Nvidia ...</a></li>
<li><a href="https://nypost.com/2026/11/20/opinion/should-jensen-huang-return-as-nvidia-ceo-many-of-silicon-valleys-smartest-minds-are-backing-him/">Should Jensen Huang return as Nvidia CEO? Many of Silicon ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#Jensen Huang`, `#Earnings`, `#Leadership`, `#Semiconductors`

---

<a id="item-34"></a>
## [AI Face Licensing Tests Hollywood’s Consent Boundaries](https://techcrunch.com/2026/11/21/is-selling-an-ai-version-of-your-face-to-this-microdrama-startup-the-future-of-hollywood/) ⭐️ 6.0/10

An actor has licensed his face to a microdrama startup, extending a face-licensing trend already established in China to a debate about Hollywood. The arrangement illustrates how performers may authorize AI-generated digital replicas for short-form drama production while raising questions about the durability of their consent. If face-licensing becomes standard, actors could earn revenue from synthetic performances while studios gain access to reusable digital replicas. However, the model could also normalize unclear consent terms, broader reuse of a performer’s likeness, and displacement of human actors as AI video becomes cheaper and more realistic. The reported deal concerns an actor’s face rather than a full acting performance and has not yet demonstrated Hollywood-wide adoption. Relevant safeguards include the scope and duration of consent, permitted uses, compensation, revocation rights, and whether the deal covers a named actor or a reusable digital replica; the available summary does not specify those terms.

rss · TechCrunch AI · Nov 21, 16:00

**Background**: Microdramas are short-form episodic dramas designed for social-media platforms, where AI can reduce production costs by automating visual production and adapting existing content. China is described as the origin of both the microdrama industry and a face-licensing model, and some startups also use AI to convert long-form dramas into microdramas. Licensing a likeness can provide legitimate consent, but it does not by itself establish how long authorization lasts or how broadly the resulting replica may be used.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/21/is-selling-an-ai-version-of-your-face-to-this-microdrama-startup-the-future-of-hollywood/">Is selling an AI version of your face to this microdrama ... | TechCrunch</a></li>
<li><a href="https://www.storyboard18.com/how-it-works/indias-microdrama-startups-bet-on-ai-to-slash-production-costs-by-75-84105.htm">India&#x27;s microdrama startups bet on AI to slash... - Storyboard18</a></li>
<li><a href="https://www.businessinsider.com/actors-sexualized-fake-ads-promote-micro-dramas-tiktok-meta-2026-5">Actors Call Out Promos With Fake Sex Scenes... - Business Insider</a></li>

</ul>
</details>

**Tags**: `#AI-generated content`, `#digital replicas`, `#Hollywood`, `#licensing`, `#actor consent`

---

<a id="item-35"></a>
## [Super El Niño Could Intensify Global Hunger](https://www.wired.com/story/how-this-years-super-el-nino-will-worsen-global-hunger/) ⭐️ 6.0/10

A projected super El Niño could intensify droughts and crop losses in vulnerable countries, worsening food insecurity already aggravated by war and cuts to foreign aid. Some regions may become wetter, but the uneven distribution of rainfall could leave millions without sufficient food. The combination of climate shocks, conflict, and reduced humanitarian funding could turn an agricultural and water crisis into a broader hunger emergency. The effects are likely to fall disproportionately on countries with limited resources and fewer coping mechanisms. A super El Niño is characterized by tropical Pacific temperatures more than 2°C above average, potentially producing more persistent droughts, floods, extreme heat, and disruptions to food production than typical El Niño events. Historical patterns and global forecasting models indicate that heat, drought, and floods can reduce staple-crop yields in certain regions.

rss · Wired · Nov 22, 10:00

**Background**: El Niño is a climate pattern that alters atmospheric circulation and rainfall across multiple regions. Its impacts are uneven: some areas receive heavier rainfall, while others experience severe drought and heat that can strain water supplies, livestock, and crop yields. Because countries already affected by war and aid cuts may have little capacity to absorb another shock, a strong El Niño can compound existing food-security risks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wri.org/insights/super-el-nino-impacts-explained">2026 Super El Niño Impacts, Explained | World Resources Institute</a></li>
<li><a href="https://ua-gwsc.org/how-could-el-nino-affect-global-food/">How could El Niño affect global food ? – Global Water Security Center</a></li>
<li><a href="https://www.wired.com/story/how-this-years-super-el-nino-will-worsen-global-hunger/">How This Year’s Super El Niño Will Worsen Global Hunger | WIRED</a></li>

</ul>
</details>

**Tags**: `#El Niño`, `#Climate Change`, `#Food Security`, `#Global Hunger`, `#Climate Policy`

---

<a id="item-36"></a>
## [ESA Probe Revisits NASA’s Asteroid Defense Test Site](https://www.wired.com/story/a-space-probe-returns-to-astroids-where-nasa-tested-planetary-defense-systems/) ⭐️ 6.0/10

ESA’s Hera probe is returning to the Didymos system to investigate the asteroid system affected by NASA’s DART mission. Its observations will examine the changes produced when DART struck the smaller asteroid Dimorphos in September 2022. Hera provides an opportunity to evaluate the effects of a real kinetic-impact deflection attempt, rather than relying only on simulations. The results could improve NASA and ESA’s ability to assess and potentially deflect future asteroid threats. NASA’s DART spacecraft intentionally collided with Dimorphos, a moonlet of the larger asteroid Didymos, to change its motion. ESA’s Hera spacecraft, launched in 2024, is surveying the binary asteroid system and examining what DART’s impact altered; the available update does not report new findings yet.

rss · Wired · Nov 21, 12:00

**Background**: Planetary defense seeks to identify dangerous asteroids and alter their trajectories so they do not strike Earth. NASA’s Double Asteroid Redirection Test was the first full-scale test of a kinetic impactor against an asteroid, while Hera is the follow-up investigation of Dimorphos and Didymos.

<details><summary>References</summary>
<ul>
<li><a href="https://www.accuweather.com/en/space-news/nasas-dart-mission-successfully-changed-the-motion-of-an-asteroid/1261775">NASA &#x27;s DART mission successfully changed the motion of an asteroid</a></li>
<li><a href="https://www.undiscoveredamerica.tv/5-ways-dart-proved-humanity-can-move-an-asteroid/">5 Ways DART Proved Humanity Can Move an Asteroid</a></li>
<li><a href="https://www.sciencedaily.com/releases/2026/11/261106174532.htm">A nuclear blast could save Earth from an asteroid , but... | ScienceDaily</a></li>

</ul>
</details>

**Tags**: `#planetary defense`, `#asteroid exploration`, `#NASA`, `#ESA`, `#space research`

---

<a id="item-37"></a>
## [Large-Language-Model Pre-training Still Shows Scaling Gains](https://sebastianraschka.com/blog/2026/pretraining-is-still-not-plateauing.html) ⭐️ 6.0/10

Sebastian Raschka argues that large-language-model pre-training has not reached a performance plateau. The post presents this as an ongoing scaling trend, although the supplied excerpt does not include its supporting experiments, figures, or technical evidence. If pre-training continues to yield predictable improvements from larger models, more data, and additional compute, labs may still gain model capability through scale rather than relying exclusively on post-training methods. The claim also influences expectations about training costs, infrastructure demand, and the allocation of research effort across the model-development pipeline. The supplied material provides no benchmark results, scaling curves, model sizes, dataset sizes, compute budgets, or comparison of pre-training against test-time compute and post-training. Consequently, the post&\#x27;s central claim cannot be independently evaluated from the excerpt, and the distinction between absolute performance gains and diminishing returns per unit of compute also remains unclear.

rss · Hacker News \(best\) · Nov 22, 23:43

**Background**: Pre-training is the initial phase in which a language model learns general language patterns from a large dataset. Scaling laws describe how model intelligence and accuracy can improve predictably as parameter count, training data, and computational resources increase. A plateau can mean either that additional pre-training no longer improves performance or that the gains achieved per dollar or unit of compute are shrinking, so the meaning matters when assessing the claim.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/ai-scaling-laws/">How Scaling Laws Drive Smarter, More Powerful AI | NVIDIA Blog</a></li>
<li><a href="https://arxiv.org/pdf/2509.05258">Scaling Performance of Large Language Model Pretraining</a></li>
<li><a href="https://www.junglans.in/blog/llm-pretraining-alignment-tuning">The End-to-End LLM Pipeline: Pretraining , SFT... | Junglans Solutions</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#LLMs`, `#pre-training`, `#scaling-laws`

---

<a id="item-38"></a>
## [When Postgres Cleanup Needs a Message Queue](https://dev.to/remielbarrett8283/nodejs-postgres-cleanup-jobs-when-scheduling-should-hand-work-to-a-queue-2n0p) ⭐️ 6.0/10

The article recommends starting Postgres retention cleanup in Node.js with a scheduler and small, committed database batches. It argues that a message queue should be added only when records need independent retries, pacing, or durable recovery state. This distinction can prevent unnecessary infrastructure and operational complexity for routine database sweeps. It also helps teams identify when per-record failure isolation or external rate limits justify the additional reliability machinery of a queue. Cleanup transactions should claim a finite set of rows and delete only that set; a committed batch is durable, while an interrupted transaction rolls back and leaves remaining eligible rows for the next run. Advisory locks can prevent overlapping executions, and FOR UPDATE SKIP LOCKED can help partitioned workers avoid claiming the same rows. Queue delivery is generally at-least-once, so consumers should use the message identifier as an idempotency key and commit a completion record before acknowledging the message.

rss · Dev.to · Nov 22, 23:50

**Background**: A scheduler determines when a cleanup pass starts, whereas Postgres determines which rows that pass owns and records the transaction outcome. Message queues are designed to hold many independently recoverable work units for consumers, making them useful when records have different processing times or require isolated retries. Neither advisory locks nor row-locking clauses provide exactly-once execution for external side effects.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/pavkode/preventing-redundant-cron-job-executions-in-multi-instance-nodejs-environments-with-locking-2ofa">Preventing Redundant Cron Job Executions in Multi-Instance Node . js ...</a></li>
<li><a href="https://learn.programmingline.com/learn/system-design/system-design-message-queues-delivery-semantics-and-dead-letter-handling">Queue Delivery Semantics and DLQs | Programming Line</a></li>
<li><a href="https://codemia.io/courses/system_design_fundamentals/delivery_semantics">Delivery Semantics - Learn in this interactive lesson on Codemia.</a></li>

</ul>
</details>

**Tags**: `#Node.js`, `#PostgreSQL`, `#Job Scheduling`, `#Message Queues`, `#Distributed Systems`

---

<a id="item-39"></a>
## [Shell-Injection Scanner Adds Signed, Auditable Reports](https://dev.to/aurum_revenue/i-ran-my-shell-injection-scanner-on-my-own-repos-it-flagged-three-of-my-files-3dap) ⭐️ 6.0/10

After the author&\#x27;s own shell-injection scanner flagged three previously pushed files, they introduced \`injection-audit\`, a Python tool that produces dated, signed JSON reports with exact findings, file hashes, rule-catalog details, and stated analysis limits. The scanner uses Python AST analysis and Bash token-level heuristics to report attacker-controlled data reaching dangerous shell sinks. A one-time clean scan is weak evidence because it becomes stale as code changes and cannot independently demonstrate what was checked. Signed reports tied to repository content hashes can provide verifiable evidence for customers and security reviews, although they still need integration into continuous enforcement workflows such as CI/CD security gates. The MIT-licensed tool uses only the Python standard library and has 126 tests; it supports \`init-key\`, \`scan\`, and \`verify\` commands. Its Python analysis is intra-procedural with bounded cross-function taint propagation, while Bash analysis is token-level rather than a full shell parse; container and attribute alias tracking is limited, and lambda and comprehension bodies are skipped.

rss · Dev.to · Nov 22, 23:42

**Background**: Shell injection occurs when untrusted input is incorporated into a command executed by a shell without adequate sanitization. Static scanners identify potential data flows from attacker-controlled sources to dangerous execution sinks, but their findings require engineering judgment and cannot establish exploitability in every deployment. Auditable evidence should bind a report to the exact analyzed code and disclose both the applied rules and the analyzer&\#x27;s limitations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.onekey.com/resource/shell-cgi-static-code-analysis---automatic-discovery-of-rces">Shell CGI Static Code Analysis - Automatic Discovery of RCEs</a></li>
<li><a href="https://dl.acm.org/doi/full/10.1145/3715001">A Container Security Survey: Exploits, Attacks, and Defenses</a></li>

</ul>
</details>

**Tags**: `#application-security`, `#shell-injection`, `#static-analysis`, `#secure-sdlc`, `#ci-cd`

---