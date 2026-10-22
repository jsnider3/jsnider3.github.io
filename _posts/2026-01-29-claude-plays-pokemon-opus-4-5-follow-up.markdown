---
layout: post
title:  "Claude Plays Pokemon: Opus 4.5 Follow-up"
date:   2026-01-29 06:00:00
categories: AI
---

*Originally posted on [LessWrong](https://www.lesswrong.com/posts/gogZyeistdaDFuhbG/claude-plays-pokemon-opus-4-5-follow-up).*

[ClaudePlaysPokemon](https://www.twitch.tv/claudeplayspokemon) is a simple test of the question "Can the LLM Claude beat Pokemon Red?". As new Claude models have been released, we have gotten closer to answering that question with "yes". Similar projects with other models are also common, but they use harnesses that give the models significantly more help with the task, and therefore I think, and many others agree, that ClaudePlaysPokemon represents the best test of underlying LLM progress.

I'm not the only LessWronger to want to write about it either. [Insights into Claude Opus 4.5 from Pokémon](https://www.lesswrong.com/posts/u6Lacc7wx4yYkBQ3r/insights-into-claude-opus-4-5-from-pokemon) was written two months ago, two weeks after Opus 4.5 was released. It was a great read at the time, but in the fast-moving world of AI, many of its conclusions have been overcome by events and I wanted to give a quick overview of those updates while we wait for the next Claude to be released and make this all even more obsolete.

The original article was published after 48,000 steps when Claude was stuck in Silph Co and had been for some time. After the article was published, Claude proceeded to beat Silph Co, do Safari Zone, get stuck in Pokemon Mansion and then complete it, get all eight badges, and then go to Victory Road, where he is currently stuck trying to complete the boulder puzzles at 230,000 steps.

Let's list the key points from the original article, so we can see which still hold up and which need an update:

* Claude has better vision
* Improved spatial awareness
* Improved use of context window
* Improved ability to notice he's stuck in loops and get out of them
* Obviously not human
* Still gets pretty stuck
* He really needs his notes
* Long-term planning is poor

These points largely hold up, but I want to emphasize that the improved vision is still pretty bad and this is a genuine problem. Anthropic hasn't made fixing this a priority (which can be seen in Dario's comment at Davos that they would buy an image model if they really needed it)[^sqg68dn3p5], but that might turn out to be a mistake. I have short timelines, so even if Anthropic could get a better image model in a month, if they wait until they need one to start, that will be a significant chunk of time in a critical moment where they won't have much time left.

On his first visit to the Safari Zone, he ignored the Gold Teeth, which you need to trade to the Safari Warden to get the HM for STRENGTH. Without STRENGTH, he can't push the boulders in Victory Road to solve those puzzles and beat the game. This kind of multistep dependency would have stopped many earlier LLMs entirely and the mistake would have been irrecoverable even for some of them who could have done it, but fortunately, after beating Pokemon Mansion, he realized he needed to backtrack and was able to do it quickly. This was a clear failure in long-term planning, but one he was able to recover from when he needed to.

The main takeaway is that persistence does wonders. A human with Claude's skill issues would have given up long before victory, but Claude overcame his issues by just not giving up even after spending weeks at seemingly insurmountable obstacles. Viewers would routinely write the run off as doomed and call for dev intervention, only for Claude to stumble into the solution eventually.

I apologize for not expanding this post more, but I wanted to get it out before the next Claude is released and ClaudePlaysPokemon is reset to switch to the newer model. I'd expect Claude to beat the game given unlimited time, but the rumor mill (and [this Manifold market](https://manifold.markets/BenAybar/will-anthropic-release-claude-sonne)) is making me think that won't be very long for either of us.

[^sqg68dn3p5]: I can't find a full transcript for the Bloomberg interview which I believe he said this during, so this might be a misremembering on my part. I will edit this when I find the specific thing he said and when.
