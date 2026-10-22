---
layout: post
title:  "Can an LLM make a feature-length movie on its own?"
date:   2026-07-22 06:00:00
categories: AI
---

*Originally posted on [LessWrong](https://www.lesswrong.com/posts/24RKHEkwgZ6Hm6ygY/can-an-llm-make-a-feature-length-movie-on-its-own).*

## How it did

Betteridge's Law of Headlines says the answer is no[^7vtp0asvk02], but I was able to make a feature-length adaptation of William Hope Hodgson's *The House on the Borderland.*

<iframe width="560" height="315" src="https://www.youtube.com/embed/E7H0KFVQyV4" frameborder="0" allowfullscreen></iframe>

I have a YouTube channel where I mostly get LLMs to write albums and make them into music videos. This naturally made me curious whether an LLM could make a feature-length movie on its own. It doesn't seem like it would be harder to do than to disprove the Jacobian conjecture[^8tpjtz35ylk] and if the challenge is to just work for a long time, it should be noted that METR's time-horizon benchmark is saturated.[^nino52mbmb]

Even with my assistance, I would still say the result is a failure. It's good enough that I'm willing to put my name to it as the first feature-length movie I've made, but that is judging by the standards of small YouTube channels, not movies as an overall category.

## Why I think it failed

I would not say agency is an obstacle for this work. Claude Fable 5 knew what to do and when I gave it permission it was perfectly capable of babysitting hours of video-generation runs, debugging API issues and pipeline bugs, coming up with and implementing edits to the storyboard, and many other tasks without oversight. The main obstacles were LLMs' poor sense of timing, struggles with audio and vision, poor integration of multimodality, and losing details after lengthy sessions.

### Timing issues

The initial storyboard done by Claude Fable 5 had a runtime of 49 minutes, despite being told it was to make a feature-length movie of a book that has 50,945 words and takes 5 hours as an audiobook. GPT 5.6 Sol reviewing the storyboards didn't think the runtime was problematic either. I eventually got it to rewrite the storyboard for an hour and forty-five minutes, which seems both appropriate for a movie and adapts the book without being consistently too fast or too slow. These timing issues recur at the smaller level just as much. I had to repeatedly correct the model when it tried to fit multiple beats of action as well as dialog within eight-second shots and scripted thirty seconds of narration over forty seconds of footage.

### Video is expensive

Throughout this project, I was using Fable and Sol with very little restraint and under the (very affordable to me) $200/month subscription plans.[^tntl0vypb8] Video is much more expensive: at Gemini Omni Flash's current price of $0.10/second, it would cost $645.40 to generate this movie, but that would balloon massively to $5,146.10 when you add in the 45,007s of footage I generated which didn't make the cut[^k4olxkzl9gq]. Compared to an actual Hollywood movie, that's a bargain, but again this was done on the budget of a hobbyist YouTube channel.

### Video generators are still pretty bad

Omni Flash may be the best video generator[^0u55t7fjcpj], but there are still hard limits on its quality. For one, the inability to extend its clips means that it can only be used for short videos of between 4 and 12 seconds. I used Veo 3.1 for the rest of the film and that had recurring issues: the book's swine-things routinely came out looking like literal pigs, left/right were routinely confused, telling the model not to include something rarely worked, faces were a constant struggle, action clips routinely had beats dropped, dialog was routinely given to the wrong character, and there were frequent unnecessary cuts and dissolves. This interacts with the timing issues mentioned earlier very poorly. Fable struggles to write prompts for Veo that match the length of the video generated and Veo punishes prompts that give it too much and too little to do on-screen very heavily. We could reroll shots with all those issues, but shots that failed the first time were much more likely to fail the second time. If you see issues in the YouTube video, rest assured that those issues survived even more than two generation attempts. This all means that we hit diminishing returns hard after massive effort, but before we actually do a good job.

### Coordination difficulties

I wasn't using one large model to do all this work; it was a combination of Claude Fable 5 (coding, coordinating the others, reviewing their work), GPT 5.6 Sol (for grunt work that needed to be done at high quality), Claude Sonnet 5 (for independent perspectives on reviews), Gemini 3.5 Flash (for video review), Whisper (for audio review), Nano Banana 2 (for creating Veo's keyframes and reference images), gpt-image-2 (for editing reference images), edge-tts (for narration voice-overs), Suno v5.5 (for soundtrack), Gemini Omni Flash (for high-quality standalone clips), Veo 3.1 - Fast (for mid-quality chains of clips), and Veo 3.1 - Lite (for cheap video generation). That is literally twelve models from five companies. Even if you assume that each model could do its work without errors[^xmd5cui4j7h], there were still large time sinks where Fable would describe what it wants to Suno or Veo, get back mediocre work, struggle to verify its quality, and have trouble deciding whether the issue was with the instructions it gave or the other model struggling.

### Forgetfulness and context rot

The final issue I encountered was LLMs losing details of the work I requested them to do while working on it. After watching a cut of the movie, I would typically have around 400 lines commenting what I thought was wrong and ask them to fix it. None of the work should have been too difficult for them, but they would usually focus on the big classes of problems first and after those were dealt with, they would assume the work was done instead of checking the full list for remaining work. To me, this seemed more like them losing things in the long-context, not a knowing attempt to reward-hack or pass incomplete work off as complete, but the end result was the same, in that my third or fifth watch saw errors that I already reported and expected to be fixed in earlier watches.

## Where we go from here

I expect these issues to all be fixed by the end of 2027. It's a running gag that Claude gives wildly wrong estimates for how long software projects take and we can see similar issues elsewhere; an AI deficiency with such a wide impact is certainly one that will see major effort to resolve once it becomes *the* obstacle to anything important. I have full confidence that it will be solved, both from looking at lines on the graph and from comparing it to prior issues that were also solved. I'm open to work if you know a company hiring to fix these issues, but I have some ideas of my own. As for multimodality, I'm not sure whether the solution is just one god-model that can storyboard movies, write code, generate video, and refine all these outputs all on its own or for models to get better at coordinating with other specialized models, but I don't see a wall. Not until we hit the singularity.

My current goal with the video pipeline is to create movie adaptations of every classic sci-fi novel (i.e. the ones that are public domain). I think that's doable by end-of-year; whether those movies get immediately upstaged by the next generation of models is an open question.

[^7vtp0asvk02]: And it holds here.

[^8tpjtz35ylk]: [https://x.com/\_\_alpoge\_\_/status/2079028340955197566](https://x.com/__alpoge__/status/2079028340955197566)

[^nino52mbmb]: [https://metr.org/time-horizons/](https://metr.org/time-horizons/)

[^tntl0vypb8]: If you check out my [Straude](https://straude.com/u/joshuasnidercom), I probably used $5,000 of tokens, but the actual subscriptions are $200/month.

[^k4olxkzl9gq]: The full details are that the final cut is 6,454s of runtime, made from 849 clips and the rejects are 5,509 clips with 45,007s of runtime, which means there are 6,358 clips in total with 51,461s of runtime. Thus only about 13% of the clips I made were included in the final cut.

[^0u55t7fjcpj]: As of 2026/07/22, it's listed #1 on [https://artificialanalysis.ai/video/leaderboard/text-to-video](https://artificialanalysis.ai/video/leaderboard/text-to-video)

[^xmd5cui4j7h]: Which you can't.
