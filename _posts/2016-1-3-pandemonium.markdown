---
layout: post
title:  "Optimal Placement of Research Centers in Pandemic"
date:   2016-1-3 12:00:00
forcenext: "//america.joshuasnider.com/blog/"
forcenexttitle: "The World's Countries Sorted by Americanness"
comments: True
categories: update
---

<iframe src="https://ghbtns.com/github-btn.html?user=jsnider3&repo=pandemonium&type=star&count=true" frameborder="0" scrolling="0" width="170px" height="20px"></iframe>

###Updated: 2015/1/7

Pandemic[^1] is a great board game, where the players represent
agents of the Center for Disease Control and must work together
to stop four epidemics from growing out of control. Players
can build research centers which allow you to make cures for the
disease as well as allowing them to travel around the world faster.
The placement of these research centers is an important aspect of
the game's strategy and I'll introduce a set of placements which are
arguably optimal.

<img src="/pictures/pandemicMap.jpg" alt="Base map" height="250px" width="500px"/>

I would be remiss if I didn't mention Matt Wigway's
[prior work](http://www.indicatrix.org/2014/03/26/overanalyzing-board-games-network-analysis-and-pandemic/).
What he did was make a graph out of the cities and connections in Pandemic
and use NetworkX to find the centrality of each node. In layman's terms,
a city's centrality is how close it is to being the center of the universe.
With no other information, this is a good measure for determining which of
two cities would be better to put a research center in. My replicated
results[^2] are listed below from least to most central. As you
can see, there's a very strong correlation between a node's degree and
centrality. The correlation is 0.58 with a very strong
p-value of 1.33e-05.

City | Centrality | Number of neighbors
---- | ---------- | -------------------
Santiago | 0.0062 | 1
Johannesburg | 0.015 | 2
Buenos Aires | 0.020 | 2
Kinshasa | 0.020 | 3
Lagos | 0.025 | 3
Lima | 0.027 | 3
Atlanta | 0.038 | 3
Montreal | 0.040 | 3
Sao Paulo | 0.040 | 4
Washington | 0.041 | 4
Miami | 0.043 | 4
Bogota | 0.045 | 5
Khartoum | 0.047 | 4
New York | 0.055 | 4
Beijing | 0.056 | 2
Osaka | 0.064 | 2
Mexico City | 0.065 | 5
London | 0.071 | 4
Essen | 0.073 | 4
St. Petersburg | 0.074 | 3
Seoul | 0.074 | 3
Milan | 0.075 | 3
Chicago | 0.080 | 5
Madrid | 0.086 | 5
Los Angeles | 0.088 | 4
Moscow | 0.093 | 3
Paris | 0.096 | 5
Tokyo | 0.097 | 4
Algiers | 0.11 | 4
San Francisco | 0.11 | 4
Riyadh | 0.12 | 3
Sydney | 0.13 | 3
Cairo | 0.14 | 5
Istanbul | 0.16 | 6
Shanghai | 0.17 | 5
Tehran | 0.17 | 4
Mumbai | 0.17 | 3
Taipei | 0.18 | 4
Baghdad | 0.19 | 5
Karachi | 0.21 | 5
Jakarta | 0.22 | 4
Manila | 0.23 | 5
Ho Chi Minh | 0.25 | 4
Delhi | 0.26 | 5
Kolkata | 0.27 | 4
Chennai | 0.29 | 5
Bangkok | 0.31 | 5
Hong Kong | 0.33 | 6

However, what we're interested in is a set of n cities that together
are the best places to put research centers, not a single best city.
As our constraints, we only care about sets of
size greater or equal to one and less than or equal to six as we don't have
enough pieces to have more than six research centers and we are given a
mandatory free one in Atlanta.

How can we compare two proposed placements? The most intuitive measure for
me is the average distance from each city in the world to the nearest
research center. According to
[Stack Exchange](http://math.stackexchange.com/q/1309646/), this is
reducible to the problem of finding a dominating set which is known to
be NP-Hard. Fortunately, this problem (despite being NP-Complete) is
solvable in reasonable time for a problem as small as ours. Especially
when you cache the all-pairs shortest paths matrix.

Obviously, with only one research center the only possible placement is
Atlanta which is therefore optimal.

With two research centers the optimal solution is to pair Atlanta with
either Baghdad or Cairo. Looking at the solution for two centers, one might
think it would be better to do Atlanta and Karachi instead since that is
seven away from Atlanta traveling both East and West, whereas Atlanta is
five away from Cairo one way and nine away from Cairo the other way. This is
a good intuition, but unfortunately the average distance for Atlanta and
Karachi is 1% higher. Moving to Karachi makes you slightly closer to places
like Jakarta, but it also makes you slightly farther away from places like
Kinshasa and Essen and the trade off is just barely not worth it.[^3]

<img src="/pictures/pandemicMap2.jpg" alt="Two centers" height="250px" width="500px"/>

With three research centers there's one optimal solution with the mandatory
Atlanta, Hong Kong covering East Asia, and Cairo providing fast travel to
Africa, Europe, and the Mideast.

<img src="/pictures/pandemicMap3.jpg" alt="Three centers" height="250px" width="500px"/>

With four research centers, we take the optimal solution for three, move
our Mideast center to Istanbul and put our fourth in Sao Paulo to cover
the southwest side of the globe.

<img src="/pictures/pandemicMap4.jpg" alt="Four centers" height="250px" width="500px"/>

With five research centers, we have seven equally good choices.
Each involves placing one in Atlanta, one in Europe, one in
South America, one in East Asia, and one in either the Middle East
or South Asia.

North America | Europe | East Asia | Mid east | South America
------------- | ------ | --------- | -------- | -------------
Atlanta       | Istanbul | Shanghai | Chennai | Sao Paulo
Atlanta       | Istanbul | Hong Kong | Delhi  | Sao Paulo
Atlanta       | Istanbul | Hong Kong | Karachi | Sao Paulo
Atlanta       | Paris  | Hong Kong | Baghdad  | Bogota
Atlanta       | Paris  | Hong Kong | Cairo    | Bogota
Atlanta       | Essen  | Hong Kong | Cairo    | Bogota
Atlanta       | London | Hong Kong | Cairo    | Bogota

<img src="/pictures/pandemicMap5.jpg" alt="Five center example" height="250px" width="500px"/>

Finally, with six research centers we can cover all corners of the
globe with Atlanta, Paris, Khartoum, Hong Kong, Karachi, Bogota.
As per the rules,[^4] you can only have six research centers, so when you
try to build a seventh you have to get rid of one of your existing
stations. There's a slight advantage to removing your Atlanta station
and replacing it with one in Chicago.

<img src="/pictures/pandemicMap6.jpg" alt="Six centers" height="250px" width="500px"/>

Of course, if we build a research center in Cairo we can't move it
to Istanbul until we've built six of them, which means it's impossible
to solely go through the optimal layouts. Furthermore,
unless one of the players is the operations expert it's unlikely we
can build research stations in the optimal locations at will.[^5]
What we want now is a ranking of which cities are the best for research
centers and a separation of them into regions where we understand that
it's never a good deal to put two research centers in the same region.

The centrality measure previously discussed is a good judge of how good
building a research center in a city is, but let's check our work by
counting how many times each city appears in the optimal placements.

City | Occurences
---- | ----------
Shanghai | 1
Chennai | 1
Delhi | 1
Khartoum | 1
London | 1
Essen | 1
Baghdad | 2
Karachi | 2
Paris | 3
Istanbul | 4
Sao Paulo | 4
Bogota | 5
Cairo | 5
Hong Kong | 9
Atlanta | 13

The correlation between the number of occurences and the centrality
measure depends a lot on whether we include Atlanta. With it the
correlation rounds to 0.10 and is not statistically significant. Without
it the correlation jumps to 0.27 with a p-value of 0.07. The likely 
reason these measures aren't better correlated is because a lot of the
most central cities are clustered together in Asia while optimal
placement is based on spreading out.

One way we can separate the world into regions is with a Voronoi
diagram where each research center in the optimal six center layout
is the center of a zone.  
**Central Asia**: Moscow, Delhi, Baghdad, Tehran, Karachi, Riyadh, Mumbai  
**Europes**: Istanbul, Paris, St. Petersburg, London, Algiers, Milan, Madrid,
  Essen  
**Africa**: Kinshasa, Johannesburg, Khartoum, Lagos, Cairo  
**Latin America**: Mexico City, Sao Paulo, Santiago, Buenos Aires, Lima,
  Bogota  
**North America**: Chicago, San Francisco, Los Angeles, Atlanta, Miami,
  Montreal, Washington, New York  
**East Asia**: Manila, Shanghai, Sydney, Kolkata, Chennai, Seoul, Bangkok,
  Taipei, Hong Kong, Ho Chi Minh, Tokyo, Jakarta, Beijing, Osaka

Of course, we've artificially constricted ourselves by always having
a research center in Atlanta. Is it possible to come to a better solution
by relaxing that requirement? What if we've already been forced to put
a research center in Santiago? Where should we put the rest of our
stations if we've already made suboptimal moves? These are the kinds of
questions that might be covered in the future. A useful app to make based
off this work would be a REST API that tells you the average distance
for the globe to the nearest research center of a given placement and then
a pretty web frontend that uses it.

###Update: 2015/1/7

In the base game, the above analysis isn't as useful
as it could be since you will most likely be busy
dealing with one or two diseases more than the rest.
However, in Pandemic Legacy this kind of analysis is much
more useful as it's possible to preserve a research station
across playthroughs. It also has a slightly different map,
but fortunately https://github.com/gracegallis gave that
to me through a pull request.

For Pandemic Legacy, the first four solutions are largely the
same as for the classic board. Your first station should be in Atlanta,
your second should be in Cairo, and your third should be in Hong Kong.

For four stations they should be in Atlanta, Istanbul, Sao Paulo, and
Hong Kong. The fifth when built should be in either Delhi or Karachi.

After the first five, the amount of good options you have rapidly
explodes, so I'll provide a list of cities and how often they appear
in optimal solutions.

City | Occurences
---- | ------
Cairo | 2
Chicago | 3
New York | 3
Shanghai | 6
Washington | 6
London | 8
Karachi | 8
Sao Paulo | 9
Atlanta | 11
Delhi | 14
Buenos Aires | 14
Los Angeles | 15[^6]
Hong Kong | 18
Istanbul | 23

--------

**Footnotes:**

[^1]: The Pandemic board game is copyright by Z-Man Games.
[^2]: I was actually planning to do the analysis he did, but after seeing he already did it, I expanded it to this.
[^3]: This was suggested by u/Robinetski on Reddit. It's a good suggestion.
[^4]: I was initially unaware of this rule and was corrected by u/Erdomas on Reddit. The Reddit discussion can be found <a href="https://www.reddit.com/r/boardgames/comments/3zeay6/optimal_placement_of_research_centers_in_pandemic/">here</a>.
[^5]: It's also common to have scenarios where you want to build a research center somewhere so that you can cure a disease as soon as possible. For example, on the day I decided to write this blog post we had our medic fly down to Lima and build a research station there because another player went down to Santiago to cure some disease and happened to draw the cards needed to make a cure.
[^6]: Mostly as a replacement to Atlanta.
