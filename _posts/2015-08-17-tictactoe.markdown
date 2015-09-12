---
layout: post
title:  "Unbeatable Tic Tac Toe"
date:   2015-08-17 12:00:00
comments: True
categories: update android gaming
---

<a href="https://play.google.com/store/apps/details?id=com.joshuasnider.tictactoe">
  <img alt="Get it on Google Play"
       src="https://developer.android.com/images/brand/en_generic_rgb_wo_45.png" />
</a>

#### Intro

I’m not a fan of mobile games that allow you to bribe your way to victory,
even though they are as reliable a business model as advertising is for
websites. I wanted to learn Android programming and making a parody of this
type of game seemed like a decent scope for a “My First Android” kind of
project. Thus, I set out to create a game of tic-tac-toe where the AI plays
 perfectly (and is therefore unbeatable) unless you pay 99 cents in which
case it plays randomly and can be beaten 99.4792%<sup>1</sup> of the time.

#### Design overview

I needed four classes for this a `TicTacToeBoard` which stored a game state,
calculated the computer’s moves, and provided a variety of library
functions, a `MainActivity` which showed the actual tic tac toe board and
had a drop down menu, an `AboutPage` which was an activity that showed some
info about me, and a `ScorePage` which was an activity that displayed the
user’s cumulative wins, losses, and draws.

When the app needed to save `MainActivity`’s state it did so by writing the
board out as 10 strings, 9 to represent the text in each space and one to
say which person had just moved, we then had two strings to say the
computer and player’s chars,<sup>2</sup> and a flag to track whether
we were in easy mode or not.<sup>3</sup>

In our long-term storage, we currently have a flag to keep track of whether
we have ever played before and integers for the user's number of wins,
losses, and draws.<sup>4</sup>

#### Challenges encountered

Making my first Android app was a quick journey, but one beset by challenges.
Most of them were due to me not yet knowing how to do Android programming,
but one or two may have been actually difficult. 

There were three bugs that troubled me long enough for me to have made a
ticket for them. First, when I was trying to set the `MainActivity` as an
`onClickListener` for the nine buttons it would crash. The fix for this was
to call `setContentView` before trying to register for those events. Second,
rotating `MainActivity`’s screen would make the tic-tac-toe board disappear.
I fixed this at first by fixing the orientation of `MainActivity`. I then
fixed it properly by making `TicTacToeBoard` implement `Parcelable` and overriding
`onSaveInstanceState` and `onRestoreInstanceState`. This solution had a bug
where pressing the Verizon button on my phone would cause it to crash,
this was just a dumb mistake in my parceling code. Third, it wouldn’t
preserve anything when I switched screens or logged in or out. This was
solved by setting `android:launchMode="singleTop"` in the manifest.<sup>5</sup>


Something I struggled with generally, but that isn’t technically a bug was
in app billing. There's a good tutorial [here](http://developer.android.com/google/play/billing/billing_integrate.html)
which was helpful at the end after I tried everything else. Testing my in-app
billing was also kinda hard, since Google doesn’t allow developers to buy
things from themselves<sup>6</sup>. What you’re supposed to do is have a
spare device with a test account installed on it. Since I currently only
own one phone, I just reached out to a friend, Kunal, who does mobile
programming and got them to be a beta tester for me. He also helped by
telling me the “best” way to fix some of the bugs I encountered in the
previous paragraph.

#### Future work

There were a lot of possible enhancements that I would or should put in a
more commercial app, but which I decided were out-of-scope for this. I should
have used a namespace for my product ID, I went with `"sku_easy_mode"` because
I saw an example somewhere using SKUs. They may have meant it in a different
way. I could have used a licensing scheme to validate that the app was
installed from the official channel, but I wasn’t convinced this would
benefit me and I ran into time constraints before getting back around to it.
I could have made some popups to talk with the user, but I felt that toasts
were sufficient for my purposes. I could have had an Unbeatable TicTacToe logo
show up, which would change into a Beatable TicTacToe logo when easy mode
was enabled. 

I might want to take the current app and just make it look prettier. The about
page could have separate text boxes for the links with thumbnail images next to
them, the score page could have big text boxes for the actual score and then a
message at the bottom making a snarky comment about the user either being bad
at the game (if they lose a lot), being just as smart as a computer (if they
mostly draw), or wasting money on tic-tac-toe (if they win a couple times with
easy mode), the main activity could have stylized text boxes to make the
tic-tac-toe board prettier and it could resize to fill the screen. I also have
an idea for a much more serious game than tic-tac-toe, but as a firm believer
that ideas are worthless and execution is everything I’ll wait to announce it
until I actually have an alpha.<sup>7</sup>

One thing I really want on Android is a music player that preserves your spot
when you pause and come back later. The default music player on my Samsung
doesn’t do that, but if you download a long audio file, say a podcast, as an
mp3 and try to listen to it in pieces it’s critical that you can find the
spot you left off easily. I’m going to look around for pre-existing work
before I do this though.

#### Lessons Learned

I needed to get a Google Play Developer account and a Google Pay Merchant
account in order to publish this app. I'm on the very edge of getting my own
LLC and officially becoming a business, but I’ll most likely delay that
until I have separate business income. 

I also learned to use a more modern IDE, most of my programming is done in
gvim, but all of the Android tutorials I read wanted me to use Android Studio
and my desire to be a rebel just wasn’t strong enough. This worked well for
me, autocompletion was a nice feature and so was being able to run an app by
clicking a button. Looking back, this project is a lot like life. I could
have done it a lot better, but I stand by the work I did.


--------

**Footnotes:**

1. This is an exact number. I know this because Jane Street had a puzzle
   to find this number in [May](https://www.janestreet.com/puzzles/solutions/may-2015-solution/).
   I have a programmatic solution [here](https://github.com/jsnider3/Workspace/blob/master/Competitive/OCaml/tictacs.ml), 
   but this can also be calculated by hand.

2. Some of that data is redundant. For example, if we know the player’s
   symbol, we can find the computer’s symbol, if we have the game board
   we can determine if X just moved by seeing if there are more X’s than O’s.
   The minimum number of bits needed to store the TicTacToeBoard is 16. One
   bit tracks whether the player is X or O, we then need `log2(3)` bits to store
   whether each of the nine spots is an X, O, or free. `log2(3) * 9+1 = 15.2646625065`
   bits, which rounds up to 16. My choice to store redundant data is solely
   because I believe that programmer time and the risk of bugs that naturally
   comes with more complex code is more expensive than disk space.

3. Tracking whether the game is currently in “easy mode” was originally
   done using `SharedPreferences`, but was refactored to be stored in
   a `Bundle` by `onSaveInstanceState` in version 1.3.2. I then used
   my Orwellian editor powers to change this blog post accordingly.

4. Of course, this means that if someone plays more than two billion times.
   Parts of their score may start to wrap around to negative two billion. If
   you plan on playing this game that much, please let me know and I will
   fix this issue.

5. I essentially had
   [this](http://stackoverflow.com/q/20819019/why-is-ondestroy-always-called-when-returning-to-parent-activity).

6. As explained in don smolen’s answer
   [here](http://stackoverflow.com/q/14139034/testing-in-app-billing-the-publisher-cannot-purchase-this-item).

7. Somewhat relevant reading is [here](http://blog.jpl-consulting.com/2012/04/why-i-wont-sign-your-nda/). 
