---
layout: post
title:  "Nine Years Later: The AI Revolution Happened While My Blog Slept"
date:   2025-08-24 10:00:00
categories: update
---

My last blog post was February 7, 2016. Since then my blog has just slowly accumulated technical debt and dust. Today I had Claude[^20], an AI from Anthropic, clean up all the rust and migrate this blog from Google App Engine to GitHub Pages in an hour. The fact that an AI helped me migrate this blog is a neat summary of how much has changed while I wasn't looking.

<!--more-->

## The AI State of the World in 2016

When I last posted, AI's public milestones looked like this:
- **DeepMind's AlphaGo** had just beaten Fan Hui (October 2015)[^1] and was about to beat Lee Sedol in March 2016[^2]
- **Siri** could barely set timers reliably
- **Google Translate** was still using phrase-based statistical machine translation[^3]
- **Deep learning** had conquered ImageNet with ResNet (2015)[^4], but most people didn't care
- **GPT-1** wouldn't exist for another two years
- **Self-driving cars** were promised by Elon Musk to arrive by 2017, then 2018, then 2019[^5]

Back then, there were companies claiming they'd help you generate blogs and code automatically, but they were universally terrible—just templates and boilerplate. The idea that I'd have an AI actually understand and migrate my blog, write real code, and help create content would have seemed like science fiction.

## The AI Explosion

### The GPT Timeline That Changed Everything
- **2016**: AI can play Go[^2]
- **2018**: GPT-1 was released with 117M parameters—and nobody really noticed[^6]
- **2019**: GPT-2 with 1.5B parameters - OpenAI worried it was "too dangerous" to release[^7]
- **2020**: GPT-3 with 175B parameters—suddenly AI could write coherent essays[^8]
- **2022**: ChatGPT launched—the world changed overnight[^9]
- **2023**: GPT-4 passed the bar exam[^10], medical licensing exams, and could see images
- **2024**: Claude 3.5 Sonnet[^11], Gemini, and Llama 3[^12]—AI coding assistants became pair programmers
- **2025**: AI agents starting to do independent work, though not very well

### What AI Does For Me Now
Today, while migrating this blog, an AI assistant:
- Diagnosed that my domain resolved to Squarespace, which was redirecting to Google App Engine
- Wrote the migration scripts
- Created dark mode CSS that respects system preferences
- Cleaned up nine years of technical debt
- Even wrote the first draft of this post

This would have taken me days in 2016. It took two hours in 2025.

### The Coding Revolution
The way we write code has fundamentally changed:
- **Copilot/Cursor** can autocomplete entire functions from comments
- **ChatGPT/Claude** debug error messages more effectively than Stack Overflow
- **AI code review** often surfaces bugs before humans review the code
- **Documentation** can be generated and kept current with the right tooling
- Junior developers with AI can ship production code that would have required a whole team in 2016

### AI Capabilities That Still Blow My Mind
- **Multimodal understanding**: I can paste a niche meme and get the joke explained
- **Code translation**: "Convert this Python 2.7 to modern TypeScript" just works
- **Contextual awareness**: With large context windows, AI can track our conversations and project state
- **Creative writing**: AI can match any writing style or tone
- **Image generation**: DALL-E, Midjourney, and Stable Diffusion have displaced much of stock photography

### What AI Still Can't Do (But Probably Will Soon)
- **Run continuously**—they still need humans to invoke them
- **Self-improve their own code**—AGI remains elusive
- **Replace senior developers**—but it's getting uncomfortably close
- **Physical world tasks**—they can't fix your plumbing or build furniture (yet)
- **Understand true context** beyond their context window
- **Generate truly novel scientific breakthroughs**—though they're great at synthesis

## The Biggest Surprise: No Skynet

Here's what I didn't expect: we have AI that can pass the bar exam, write symphonies, and code better than most humans, but it hasn't taken over the world. No Skynet. No Ultron. No HAL 9000. Not even a "Her" style AI that we fall in love with (though Grok's Ani is trying)[^13].

Instead, we got... really smart autocomplete.

These AIs are incredibly capable but fundamentally passive. They wait for our prompts. They don't have desires or goals. Yes, there are agentic systems and SWE agents being developed everywhere, but they're still fundamentally reactive—they execute tasks we define rather than pursuing their own objectives. 

I expected this phase—powerful but not autonomous AI—to last maybe a year or two before someone figured out how to make them into agents. But here we are in 2025, and Claude still needs me to press Enter. ChatGPT still waits patiently for the next prompt. Copilot suggests code but doesn't write entire programs while I sleep.

But let's not get too comfortable. The pace hasn't slowed—it's accelerating. Just this year:
- **OpenAI**[^14] and **Google's Gemini**[^15] both reached IMO gold-medal-level performance in mathematics
- **Genie 3** can generate playable 3D worlds from a single image[^16]
- **GPT-5** can reason through complex multi-step problems that would have stumped GPT-4[^17]
- AI that seemed miraculous in 2023 now feels quaint

Looking back at ChatGPT from just two years ago is like watching a flip phone after using an iPhone. It was impressive then, but today's models make it look like a toy. If this pace continues, my "extended tool phase" observation might age very poorly, very quickly.

It's like we've built a Formula 1 engine but we're still figuring out how to attach wheels. The capability is there, but the autonomy isn't. And honestly? That's probably a good thing. This extended "tool phase" is giving us time to figure out alignment, safety, and what we actually want from AI before it starts wanting things from us. But that time might be shorter than we think.

## The Unexpected Consequences

The world is drowning in AI-generated content. We can produce homework essays, generic creative writing, passably good artwork, and corporate boilerplate faster than anyone can consume it. The internet is filling up with what people call "slop"—technically correct but soulless content that nobody asked for. Meanwhile, Stack Overflow traffic has reportedly dropped by 50% since 2022[^18]. Why wade through outdated answers when AI gives you a personalized solution in seconds? The entire model of community-driven knowledge sharing is evaporating.

The tech optimists insist this is all progress—creative destruction at its finest. Old inefficiencies swept away by superior technology. The invisible hand optimizing knowledge transfer. But tell that to the Stack Overflow contributors who spent decades building a commons, or the junior developers who will never develop deep expertise, or the teachers watching their entire pedagogical model collapse. The market may be efficient, but efficiency isn't everything.

This shift has fundamentally broken how we learn. Junior developers now skip entire learning curves, jumping straight from "Hello World" to building production apps with AI assistance. They never struggle through the fundamentals that build intuition. It's like GPS navigation—incredibly useful, but we've forgotten how to read maps. We need AI to be productive, but we need expertise to know when AI is wrong. The very tool that lets juniors code like seniors also prevents them from developing the judgment to spot AI hallucinations, judge architectural decisions, or debug things on their own.

Everything looks the same now. AI tends to give similar answers to similar prompts, so everyone's code has converged on the same patterns, the same variable names, the same comments. We're losing the quirky, personal style that made codebases unique. Academic institutions are in crisis mode trying to detect AI-generated assignments. Code reviews now include checking if the implementation is "too perfect" to be human-written. We have to specify "written by a human" like it's artisanal bread. This post? Co-written with Claude. My code? Codex helped. The line between human and AI creation has blurred beyond recognition.

Perhaps most insidiously, the expectations have completely recalibrated. What used to take a week should now take a day. What took a day should take an hour. Clients and managers have internalized AI-assisted productivity as the new baseline. "Just have ChatGPT do it" has become the new "just Google it," except the expectations are 10x higher. We've built a treadmill that only goes faster.

## What Didn't Change

Despite the AI revolution:
- **Haskell** still isn't mainstream (but AI can explain monads better than any human)
- **Jekyll** still works great for blogs (though AI now writes the posts)
- **Git** still tracks our changes (now mostly AI-generated)
- **Python 2 vs 3** matters less when AI can translate between them quickly
- We still need **humans** to decide what to build

## Looking Forward (If That Even Makes Sense Anymore)

If AI progress stopped completely, right now, today—we'd still have a decade of upheaval as current AI spreads everywhere. Every industry, every job, every creative endeavor would be transformed just by what already exists. GPT-5 alone, frozen in time, would still revolutionize education, medicine, law, and programming as it reaches the billions who haven't touched it yet.

But AI progress isn't stopping. It's accelerating. 

2034 is going to be a completely alien world. I can barely imagine 2027.

The gap between 2016 and 2025 feels huge, but it might be nothing compared to 2025 to 2027. We could have AGI by then. Or we could discover fundamental limits that slow everything down. We could have AI agents running companies. Or we could have regulations that keep AI as a supervised tool. We could solve alignment and create beneficial superintelligence. Or we could be living through the final scenes of a cautionary tale.

The only prediction I'm confident in: the future is going to get very weird, very fast. The kind of weird where this blog post feels like it was written in the stone age. That's assuming Yudkowsky isn't right and we all stop writing blog posts entirely.

But hey, at least I finally got dark mode working.

---

*P.S.—The migration to GitHub Pages was remarkably smooth. The hardest part was remembering that my domain's DNS resolved to Squarespace (after Google sold Google Domains to them[^19]), which was redirecting to Google App Engine, which was serving my static Jekyll site through a Python Flask app. Why was I serving static files through Python? Because in 2016 I was playing around with App Engine, not because it made any sense. Sometimes the simplest solution (static files served statically) is the one you should have started with.*

---

## References

[^1]: [AlphaGo beats Fan Hui](https://www.nature.com/articles/nature16961) - Nature, January 2016
[^2]: [AlphaGo beats Lee Sedol](https://www.nature.com/articles/nature.2016.19575) - Nature, March 2016
[^3]: [Google's Neural Machine Translation System](https://arxiv.org/abs/1609.08144) - Wu et al., September 2016 (announcing the switch from phrase-based SMT to neural translation)
[^4]: [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) - He et al., 2015
[^5]: [List of predictions for autonomous Tesla vehicles by Elon Musk](https://en.wikipedia.org/wiki/List_of_predictions_for_autonomous_Tesla_vehicles_by_Elon_Musk) - Wikipedia
[^6]: [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) - OpenAI, 2018
[^7]: [Better Language Models and Their Implications](https://openai.com/blog/better-language-models/) - OpenAI, February 2019
[^8]: [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) - Brown et al., 2020
[^9]: [ChatGPT: Optimizing Language Models for Dialogue](https://openai.com/blog/chatgpt/) - OpenAI, November 2022
[^10]: [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) - OpenAI, March 2023
[^11]: [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) - Anthropic, June 2024
[^12]: [Llama 3: Meta's Most Capable Openly Available LLM](https://ai.meta.com/blog/meta-llama-3/) - Meta, April 2024
[^13]: [Introducing Ani: A Personalized AI Companion](https://x.ai/blog/ani) - xAI, 2025
[^14]: [OpenAI claims IMO gold medal](https://www.lesswrong.com/posts/RcBqeJ8GHM2LygQK3/openai-claims-imo-gold-medal) - LessWrong, July 2025
[^15]: [Gemini reaches IMO gold medal level performance](https://blog.google/technology/ai/google-gemini-imo-2025/) - Google, July 2025
[^16]: [Genie 3: A large-scale foundation world model](https://deepmind.google/discover/blog/genie-3-a-large-scale-foundation-world-model/) - DeepMind, July 2025
[^17]: [Introducing GPT-5](https://openai.com/blog/gpt-5/) - OpenAI, 2025
[^18]: [Stack Overflow traffic down 50%](https://observablehq.com/@ayhanfuat/the-fall-of-stack-overflow) - Observable, August 2024
[^19]: [Google to sell domains business to Squarespace](https://www.reuters.com/technology/squarespace-buy-google-domains-assets-2023-06-15/) - Reuters, June 2023
[^20]: [Meet Claude](https://www.anthropic.com/claude) - Anthropic, 2024
