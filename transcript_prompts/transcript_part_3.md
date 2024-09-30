## Prompt Instruction
Please summarize the following parts of this transcript:

## Chapters Included
1:05:02 - Spot robot

## Transcript
[00:56:48] And so, the kinda stuff
I'm particularly interested [00:56:51] in may not be the thing that
makes money in the short term. [00:56:54] I can make an argument
that will in the long term. [00:56:57] But the kinda stuff I've been
playing with is a robust way [00:57:02] of having the quadrupeds, the
robot dogs communicate emotion [00:57:07] with their body movement- [00:57:08] - Hmm.
- the same kinda stuff [00:57:09] you do with a dog- [00:57:10] - Yeah.
- but not hard coded, [00:57:13] but in a robust way-
- Mm-hmm. [00:57:15] - and be able to communicate
excitement, or fear- [00:57:17] - Mm-hmm. [00:57:18] - boredom, all these kinds of stuff. [00:57:20] And I think as a base layer
of function, of behavior [00:57:26] to add on top of a robot, I think that's [00:57:28] a really powerful way [00:57:30] to make the robot more usable for humans, [00:57:33] for whatever application.
- I think it's gonna be [00:57:34] really important, and it's
a thing we're beginning [00:57:38] to pay attention to. [00:57:42] A differentiator for the
company has always been [00:57:45] we really want the robot to work. [00:57:47] We want it to be useful. [00:57:50] Making it work at first meant [00:57:52] the legged locomotion really works. [00:57:54] It can really get around,
and it doesn't fall down. [00:57:58] But beyond that, now it
needs to be a useful tool. [00:58:02] And our customers are, for
example, factory owners, [00:58:06] people who are running a
process-manufacturing facility. [00:58:09] And the robot needs to be able to get [00:58:11] through this complex
facility in a reliable way, [00:58:14] you know, taking measurements. [00:58:17] We need for people who
are operating those robots [00:58:21] to understand what the robots are doing. [00:58:23] If the robot needs help
or, you know, is in trouble [00:58:28] or something, it needs
to be able to communicate [00:58:31] and a physical indication of some sort [00:58:35] so that a person looks
at the robot and goes, [00:58:36] "Oh, I know what that robot's doing. [00:58:38] That robot's going to go take measurements [00:58:41] of my vacuum pump with
its thermal camera." [00:58:44] You know, you wanna be
able to indicate that, [00:58:48] or even just the robot's
about to turn, you know, [00:58:52] in front of you and
maybe indicate (laughs) [00:58:54] that it's going to turn. [00:58:55] And so, you sort of see and
can anticipate its motion. [00:58:58] So, this kind of communication is going [00:59:00] to become more and more important. [00:59:02] It wasn't sort of our
starting point, you know, [00:59:06] but now the robots are
really out in the world, [00:59:09] and you know, we have about 1,000 of 'em [00:59:11] out with customers right now. [00:59:14] This layer of physical indication,
I think, is gonna become [00:59:19] more and more important. [00:59:21] - We'll talk about where it goes [00:59:23] 'cause there's a lot of
interesting possibilities. [00:59:24] But if you can return back to
the origins of Boston Dynamics [00:59:28] with the more research, the R&D side, [00:59:31] before we talk about how
to build robots at scale. [00:59:36] So, BigDog. [00:59:37] What's-
- So- [00:59:38] - Who's BigDog? [00:59:39] - So, the company started in 1992, [00:59:44] and in probably 2003, [00:59:50] I believe, is when we
took a contract from, [00:59:55] so, basically, 10 years, 11
years we weren't doing robotics. [01:00:00] We did a little bit of robotics with Sony. [01:00:02] They had Aibo. [01:00:03] They had their Aibo robot. [01:00:05] We were developing some software for that. [01:00:06] That kinda got us a little bit involved [01:00:08] with robotics again. [01:00:10] Then, there was this opportunity
to do a DARPA contract [01:00:13] where they wanted to build a robot dog. [01:00:17] And we won a contract to build that. [01:00:21] And so, that was the genesis of BigDog, [01:00:24] and it was a quadruped,
and it was the first time [01:00:27] we built a robot that
had everything on board. [01:00:29] You could actually take the robot [01:00:31] out into the wild and operate it. [01:00:32] So, it had an onboard power plan. [01:00:34] It had onboard computers. [01:00:36] It had hydraulic actuators
that needed to be cooled. [01:00:40] So, we had cooling systems built in, [01:00:43] everything integrated into the robot. [01:00:45] And that was a pretty rough start, right? [01:00:48] It was 10 years that we
were not a robotics company. [01:00:52] We were a simulation
company, and then we had [01:00:53] to build a robot in about a year. [01:00:55] So, that was a little bit
of a rough transition. [01:00:58] (Lex laughs) [01:00:59] (Robert laughs) [01:01:01] - I mean, can you just
comment on the roughness [01:01:03] of that transition? [01:01:03] 'Cause BigDog, I mean, [01:01:06] this is this big
quadruped, four legs robot. [01:01:11] - We built a few different
versions of them, [01:01:13] but the very earliest ones, you
know, didn't work very well, [01:01:17] (laughs) and we would take 'em
out, and it was hard to get, [01:01:20] you know, a go-kart engine
driving a hydraulic- [01:01:25] - Oh, is that what it was? [01:01:26] (Robert laughs) [01:01:27] I was-
- And you know, [01:01:28] having that all work while trying to get, [01:01:31] you know, the robot to stabilize itself, [01:01:33] and so-
- So. [01:01:34] what was the power plan? [01:01:36] What was the engine? [01:01:37] It seemed like my vague
recollection, (laughs) [01:01:42] I don't know. [01:01:43] It felt very loud, and aggressive, [01:01:45] and kind of thrown together
is what it kind of- [01:01:48] - Oh, it absolutely was, right? [01:01:49] We weren't trying to design
the best robot hardware [01:01:52] at the time, and we wanted to
buy an off-the-shelf engine. [01:01:57] And so, many of the early
versions of BigDog had literally [01:02:02] go-kart engines or something like that. [01:02:04] Usually, it-
- It was gas powered? [01:02:05] - Yeah, a gas-powered two-stroke engine. [01:02:07] (Lex laughs) [01:02:08] And the reason why it was two stroke is [01:02:09] two-stroke engines are lighter weight, [01:02:13] and we generally didn't
put mufflers on them [01:02:15] 'cause we're trying to save the weight, [01:02:17] and we didn't care about the noise. [01:02:19] (laughing) And some of these
things were horribly loud, [01:02:21] but we're trying to manage
weight because managing weight [01:02:24] in a legged robot is always important [01:02:26] because it has to carry everything. [01:02:28] - That said, that thing was big- [01:02:30] - Well-
- what I've seen [01:02:31] the videos of.
- Yeah. [01:02:32] I mean, the early
versions, you know, stood [01:02:34] about, I don't know,
belly high, chest high. [01:02:38] You know, they probably
weighed maybe a couple [01:02:40] of hundred pounds, but
you know, over the course [01:02:44] of probably five years, we
were able to get that robot [01:02:51] to really manage a remarkable
level of rough terrain. [01:02:55] So, you know, we started out
with just walking on the flat, [01:02:57] and then we started walking
on rocks, and then inclines, [01:03:00] and then mud, and then slippery mud. [01:03:03] And you know, by the end of
that program, we were convinced [01:03:07] that legged locomotion in
a robot could actually work [01:03:11] 'cause you know, going into
it, we didn't know that. [01:03:14] We had built quadrupeds at MIT, [01:03:17] but they used a giant hydraulic
pump, you know, in the lab. [01:03:21] They used a giant computer
that was in the lab. [01:03:23] They were always tethered to the lab. [01:03:26] This was the first time
something that was sort [01:03:28] of self-contained, you know,
walked around in the world [01:03:33] and balanced, and the purpose
was to prove to ourself [01:03:36] that the legged locomotion
could really work. [01:03:38] And so, BigDog really
cut that open for us. [01:03:41] And it was the beginning of what became [01:03:43] a whole series of robots. [01:03:45] So, once we showed to
DARPA that you could make [01:03:47] a legged robot that could work, [01:03:49] there was a period at DARPA [01:03:51] where robotics got really
hot, and there was lots [01:03:54] of different programs,
and you know, we were able [01:03:57] to build other robots. [01:03:58] We built other quadrupeds
like LS3 designed [01:04:03] to carry heavy loads. [01:04:04] We built Cheetah, which
was designed to explore, [01:04:08] what are the limits to
how fast you can run? [01:04:10] You know, we began to
build sort of a portfolio [01:04:14] of machines and software that let us build [01:04:19] not just one robot, but
a whole family of robots. [01:04:21] - So, push the limits in
all kinds of directions [01:04:23] in terms-
- Yeah, [01:04:24] and to discover those principles. [01:04:25] You know, you asked earlier [01:04:26] about the art and science
of legged locomotion. [01:04:29] We were able to develop
principles of legged locomotion [01:04:32] so that we knew how to build [01:04:34] a small legged robot or a big one. [01:04:35] So, leg length, you
know, was now a parameter [01:04:39] that we could play with. [01:04:41] Payload was a parameter
we could play with. [01:04:43] So, we built the LS3, which
was an 800-pound robot [01:04:46] designed to carry a 400-pound payload. [01:04:49] And we learned the design rules, [01:04:51] basically developed the design rules. [01:04:53] How do you scale different robot systems [01:04:56] to, you know, their terrain,
to their walking speed, [01:05:00] to their payload? [01:05:02] - So, when was Spot born? [01:05:06] - Around 2012 or so, [01:05:11] so, again, almost 10 years
into sort of a run with DARPA [01:05:15] where we built a bunch
of different quadrupeds. [01:05:18] We had sort of a different thread [01:05:19] where we started building humanoids. [01:05:24] We saw that probably an end was coming [01:05:27] where the government was
gonna kind of back off [01:05:29] from a lot of robotics investment. [01:05:32] And in order to maintain
progress, we just deduced [01:05:39] that, "Well, we probably
need to sell ourselves [01:05:41] to somebody who wants to
continue to invest in this area," [01:05:44] and that was Google. [01:05:45] And so, at Google, we would
meet regularly with Larry Page, [01:05:52] and Larry just started
asking us, you know, [01:05:53] "What's your product gonna be?" [01:05:56] And you know, the logical thing, the thing [01:05:59] that we had the most
history with that we wanted [01:06:02] to continue developing was a quadruped. [01:06:05] But we knew it needed to be smaller. [01:06:07] We knew it couldn't have a gas engine. [01:06:09] We thought it probably couldn't
be hydraulically actuated. [01:06:12] So, that began the process of
exploring if we could migrate [01:06:17] to a smaller, electrically actuated robot. [01:06:21] And that was really the genesis of Spot. [01:06:24] - So, not a gas engine, and
the actuators are electric. [01:06:28] - [Robert] Yes. [01:06:29] - So, can you maybe
comment on what it's like [01:06:32] at Google working with Larry Page, [01:06:35] having those meetings, and thinking [01:06:36] of what will a robot look like
that could be built at scale, [01:06:42] like, starting to think about a product? [01:06:45] - Larry always liked the toothbrush test. [01:06:48] He wanted products that
you used every day. [01:06:54] What they really wanted was, you know, [01:06:57] a consumer-level product, [01:06:59] something that would work in your house. [01:07:03] We didn't think that was
the right next thing to do, [01:07:06] because to be a consumer-level product, [01:07:08] cost is gonna be very important. [01:07:11] Probably needed to cost
a few thousand dollars. [01:07:14] And we were building these machines [01:07:16] that cost hundreds of
thousands of dollars, [01:07:18] maybe a million dollars to build. [01:07:19] And of course, we were
only building, like, two, [01:07:24] but we didn't see how to get all the way [01:07:25] to this consumer-level product- [01:07:27] - In a short amount of time. [01:07:27] - In a short amount of time. [01:07:30] And he suggested that we make
the robots really inexpensive, [01:07:35] and part of our philosophy has always been [01:07:38] build the best hardware you can. [01:07:41] Make the machine operate
well so that you're trying [01:07:46] to solve, you know,
discover the hard problem [01:07:50] that you don't know about. [01:07:52] Don't make it harder [01:07:53] by building a crappy machine, basically. [01:07:55] Build the best machine you can. [01:07:56] There's plenty of hard problems to solve [01:07:58] that are gonna have to do [01:07:59] with, you know, underactuated
systems and balance. [01:08:03] And so, we wanted to build [01:08:04] these high-quality machines still, [01:08:06] and we thought that was important for us [01:08:08] to continue learning about really what was [01:08:11] the important parts that make robots work. [01:08:16] And so, there was a little bit [01:08:17] of a philosophical difference there. [01:08:20] And so, ultimately that's
why we're building robots [01:08:23] for the industrial sector now [01:08:24] because the industry can
afford a more expensive machine [01:08:29] because, you know, their
productivity depends [01:08:32] on keeping their factory going. [01:08:33] And so, if Spot costs, you
know, $100,000 or more, [01:08:38] that's not such a big expense to them, [01:08:41] whereas at the consumer level, [01:08:43] no one's gonna buy a robot like that. [01:08:45] And I think we might eventually get [01:08:47] to a consumer-level product
that will be that cheap, [01:08:50] but I think the path to
get in there needs to go [01:08:53] through these really nice machines [01:08:54] so that we can then learn how to simplify. [01:08:57] - So, what can you say to
almost the engineering challenge [01:09:01] of bringing down cost of a robot [01:09:06] so that, presumably, when you
try to build a robot at scale, [01:09:10] that also comes into play when
you're trying to make money [01:09:12] on a robot even in the industrial setting? [01:09:15] But how interesting, how
challenging of a thing is that, [01:09:22] in particular probably new [01:09:23] to an R&D company?
(Robert laughs) [01:09:25] - Yeah, I'm glad you
brought that last part up. [01:09:27] The transition from an R&D
company to a commercial company, [01:09:31] that's the thing you
worry about, you know, [01:09:33] 'cause you've got these
engineers who love hard problems, [01:09:35] who wanna figure out
how to make robots work. [01:09:38] And you don't know if you
have engineers that wanna work [01:09:41] on the quality, and reliability, and cost [01:09:43] that is ultimately required. [01:09:47] And indeed, you know, we have
brought on a lot of new people [01:09:49] who are inspired by those problems. [01:09:52] But the big takeaway lesson for me is [01:09:55] we have good people. [01:09:56] We have engineers who
wanna solve problems, [01:10:00] and the quality, and cost,
and manufacturability is [01:10:03] just another kind of problem. [01:10:05] And because they're so
invested in what we're doing, [01:10:09] they're interested in and will go work [01:10:10] on those problems as well. [01:10:13] And so, I think we're managing
that transition very well. [01:10:16] In fact, I'm really pleased that, I mean, [01:10:21] it's a huge undertaking by the way, right? [01:10:23] So, you know, to get reliability
to where it needs to be, [01:10:28] we have to have fleets of robots [01:10:30] that we're just operating
24/7 in our offices [01:10:34] to go find those rare
failures and eliminate them. [01:10:37] It's just a totally
different kind of activity [01:10:39] than the research activity
where you get it to work, [01:10:42] you know, the one robot you have to work [01:10:45] in a repeatable way, (laughs) you know, [01:10:47] at the high-stakes demo. [01:10:48] It's just very different. [01:10:51] But I think we're making
remarkable progress, I guess. [01:10:54] - So, one of the cool
things, I got a chance [01:10:56] to visit Boston Dynamics, and I mean, [01:11:01] one of the things that's really cool is [01:11:03] to see a large number
of robots moving about [01:11:07] because I think one of
the things you notice [01:11:10] in the research environment
at MIT, for example, [01:11:14] I don't think anyone
ever has a working robot [01:11:16] for a prolonged period of time. [01:11:18] - (laughing) Exactly. [01:11:19] - So, like, most robots
are just sitting there [01:11:21] in a sad state of despair [01:11:24] waiting to be born,
(Robert laughs) [01:11:25] brought to life for a
brief moment of time. [01:11:29] I just remember there's
a Spot robot just had, [01:11:33] like, a cowboy hat on and
was just walking randomly [01:11:36] for whatever reason. [01:11:37] I don't even know, but
there's a kind of a sense [01:11:40] of sentience to it because it doesn't seem [01:11:43] like anybody was
(laughing) supervising it. [01:11:45] - Well-
- It was just doing [01:11:46] its thing.
- I'm gonna stop [01:11:47] way short of the sentience. [01:11:48] - Sure.
- It is the case [01:11:49] that, if you come to our
office, you know, today [01:11:51] and walk around the hallways, [01:11:54] you're gonna see a dozen robots
just kind of walking around- [01:11:57] - Yes.
- all the time. [01:11:59] And that's really a
reliability test for us. [01:12:03] So, we have these robots programmed [01:12:05] to do autonomous missions, get
up off their charging dock, [01:12:09] walk around the building, collect data [01:12:10] at a few different places,
and go sit back down. [01:12:13] And we want that to be
a very reliable process [01:12:15] 'cause that's what somebody
who's running a brewery, [01:12:20] a factory, that's what
they need the robot to do, [01:12:22] and so we have to dog-food our own robot. [01:12:26] We have to test it in that way. [01:12:28] And so, on a weekly basis, we
have robots that are accruing [01:12:33] something like 1,500 or maybe
2,000 kilometers of walking [01:12:39] and you know, over 1,000
hours of operation every week. [01:12:43] And that's something that
I don't think anybody else [01:12:46] in the world can do 'cause,
A, you have to have a fleet [01:12:48] of robots to just accrue that
much information. (laughing) [01:12:51] You have to be willing to
dedicate it to that test. [01:12:57] But that's essential. [01:12:58] - [Lex] That's how you
get the reliability. [01:12:59] - That's how you get it. [01:13:00] - What about some of the cost cutting [01:13:02] from the manufacturer's side? [01:13:04] What have you learned from
the manufacturer's side [01:13:06] of the transition from R&D to- [01:13:08] - And we're still learning a lot there. [01:13:11] We're learning how to cast parts [01:13:14] instead of mill it all out
of, you know, billet aluminum. [01:13:18] We're learning how to
get plastic molded parts, [01:13:22] and we're learning about
how to control that process [01:13:24] (laughs) so that you can build [01:13:25] the same robot twice in a row. [01:13:27] There's a lot to learn there. [01:13:28] And we're only partway
through that process. [01:13:31] We've set up a manufacturing
facility in Waltham. [01:13:36] It's about a mile from our headquarters, [01:13:39] and we're doing final assembly and tests [01:13:41] of both Spots and Stretches,
you know, at that factory. [01:13:46] And it's hard because, to be
honest, we're still iterating [01:13:50] on the design of the robot. [01:13:51] As we find failures from
these reliability tests, [01:13:53] we need to go engineer
changes, and those changes need [01:13:57] to now be propagated to
the manufacturing line. [01:13:59] And that's a hard process, [01:14:01] especially when you wanna
move as fast as we do. [01:14:03] And that's been challenging. [01:14:08] You know, the folks who
are working supply chain [01:14:11] who are trying to get the
cheapest parts for us, kind [01:14:14] of requires that you buy a
lot of 'em to make 'em cheap, [01:14:17] and then we go change the
design from underneath 'em, [01:14:19] and they're like, "What are you doing?" [01:14:20] And so, you know, getting
everybody on the same page here [01:14:23] that, yep, we still need to move fast, [01:14:25] but we also need to try to
figure out how to reduce cost, [01:14:28] that's one of the challenges [01:14:30] of this migration we're going through. [01:14:32] - And over the past few years, [01:14:33] challenges to the supply chain, I mean, [01:14:36] I imagine you've been a part [01:14:37] of a bunch of stressful meetings. [01:14:38] - Yeah, things got more
expensive and harder to get, [01:14:42] and yeah, so it's all been a challenge. [01:14:44] - Is there still room for simplification? [01:14:47] - Oh, yeah, much more,
and you know, these are [01:14:49] really just the first
generation of these machines. [01:14:52] We're already thinking about
what the next generation [01:14:54] of Spot's gonna look like. [01:14:56] Spot was built as a
platform, so you could put [01:14:59] almost any sensor on it. [01:15:01] You know, we provided data communications, [01:15:03] mechanical connections, power connections. [01:15:08] But for example, in the
applications that we're excited [01:15:12] about where you're
monitoring these factories [01:15:15] for their health, there's
probably a simpler machine [01:15:18] that we could build that's
really focused on that use case. [01:15:23] And that's the difference [01:15:24] between the general-purpose
machine or the platform [01:15:28] versus the purpose-built machine. [01:15:29] And so, even though even in the factory [01:15:32] we'd still like the robot to
do lots of different tasks, [01:15:35] if we really knew on day one
that we're gonna be operating [01:15:38] in a factory with these
three sensors in it, [01:15:40] we would have it all
integrated in a package [01:15:42] that would be easier, less
expensive, and more reliable. [01:15:47] So, we're contemplating
building, you know, [01:15:49] a next generation of that machine. [01:15:50] - So, we should mention that, [01:15:52] so Spot for people who
somehow are not familiar, is [01:15:57] a yellow, robotic dog [01:16:00] and has been featured
in many dance videos. [01:16:04] It also has gained an arm. [01:16:08] So, what can you say about
the arm that Spot has, [01:16:11] about the challenges of this design, [01:16:13] and the manufacturer of it? [01:16:15] - We think the future of mobile robots is [01:16:19] mobile manipulation. [01:16:22] You know, in the past 10 years, [01:16:24] it was getting mobility to work, [01:16:26] getting the legged locomotion to work. [01:16:27] If you ask, what's the hard
problem in the next 10 years, [01:16:31] it's getting a mobile robot [01:16:33] to do useful manipulation for you. [01:16:35] And so, we wanted Spot to have an arm [01:16:37] to experiment with those problems. [01:16:42] And the arm is almost as
complex as the robot itself, [01:16:48] you know, and it's an attachable payload. [01:16:53] It has, you know, several motors, [01:16:55] and actuators, and sensors. [01:16:57] It has a camera in the end of its hand, [01:16:59] so you know, you can
sort of see something, [01:17:04] and the robot will control
the motion of its hand [01:17:06] to go pick it up autonomously. [01:17:08] So, in the same way the
robot walks and balances, [01:17:11] managing its own foot
placement to stay balanced, [01:17:13] we want manipulation to
be mostly autonomous, [01:17:17] where the robot, you indicate, [01:17:18] "Okay, go grab that bottle," [01:17:19] and then the robot will just
go do it using the camera [01:17:22] in its hand and then sort
of closing in on the grasp. [01:17:27] But it's a whole nother complex robot [01:17:29] on top of a complex legged robot. [01:17:33] And of course, we made the
hand look a little like a head, [01:17:37] (laughs) you know,
because again, we want it [01:17:40] to be sort of identifiable. [01:17:42] In the last year, a lot of
our sales have been people [01:17:46] who already have a robot now buying an arm [01:17:48] to add to that robot. [01:17:50] - Oh, interesting. [01:17:52] And so, the arm is for sale? [01:17:54] - [Robert] Oh, yeah, oh, yeah. [01:17:55] It's an option. [01:17:57] - What's the interface
like to work with the arm? [01:18:04] I could just ask that question in general [01:18:06] about robots from Boston Dynamics. [01:18:09] Is it designed to be easily [01:18:12] and efficiently operated
remotely by a human being? [01:18:15] Or, is there also the capability
to push towards autonomy? [01:18:20] - We want both. [01:18:23] In the next version of the
software that we release, [01:18:26] which will be version 3.3,
we're gonna offer the ability, [01:18:31] if you have a autonomous
mission for the robot, [01:18:34] we're gonna include the
option that it can go [01:18:36] through a door, which means
it's gonna have to have an arm, [01:18:38] and it's gonna have to use
that arm to open the door. [01:18:41] And so, that'll be an
autonomous manipulation task [01:18:44] that you can program
easily with the robot- [01:18:48] - Oh.
- strictly through, you know, [01:18:50] we have a tablet interface,
and so on the tablet, you know, [01:18:53] you sort of see the view that Spot sees. [01:18:56] You say, "There's the door handle. [01:18:58] You know, the hinges are on
the left, and it opens in. [01:19:00] The rest is up to you. [01:19:02] Take care of it."
- Oh, wow. [01:19:03] So, it just takes care of everything? [01:19:05] - Yeah. [01:19:05] So, and for a task like opening doors, [01:19:09] you can automate most of that. [01:19:11] And we've automated a few other tasks. [01:19:13] We had a customer who had [01:19:17] a high-powered breaker
switch, essentially. [01:19:20] It's an electric utility,
Ontario Power Generation. [01:19:26] And when they're gonna
disconnect, you know, [01:19:28] their power supply, right, [01:19:29] that could be a gas generator, [01:19:30] could be a nuclear power
plant, you know, from the grid, [01:19:33] you have to disconnect
this breaker switch. [01:19:35] Well, as you can imagine,
there's, you know, [01:19:37] hundreds or thousands of amps
and volts (laughing) involved [01:19:40] in this breaker switch. [01:19:42] And it's a dangerous event
'cause occasionally you'll get [01:19:44] what's called an arc flash. [01:19:45] As you just do this disconnect, the power, [01:19:48] the sparks jump across,
and people die doing this. [01:19:53] And so, Ontario Power Generation
used our Spot and the arm [01:19:58] through the interface to
operate this disconnect- [01:20:03] - That's great.
- in an interactive way. [01:20:06] And they showed it to us, and
we were so excited about it [01:20:10] and said, "You know, I bet
we can automate that task." [01:20:12] And so, we got some examples
of that breaker switch, [01:20:16] and I believe in the next
generation of the software [01:20:18] now we're gonna deliver back
to Ontario Power Generation, [01:20:21] they're gonna be able
to just point the robot [01:20:24] at that breaker. [01:20:26] They'll indicate, "That's the switch." [01:20:28] There's sort of two
actions you have to do. [01:20:30] You have to flip up this
little cover, press a button, [01:20:33] then get a ratchet,
stick it into a socket, [01:20:37] and literally unscrew
this giant breaker switch. [01:20:41] So, there's a bunch of different tasks, [01:20:43] and we basically automated
them so that the human says, [01:20:45] "Okay, there's the switch. [01:20:47] Go do that part. [01:20:49] That right there is the socket [01:20:51] where you're gonna put your tool, [01:20:52] and you're gonna open it up." [01:20:53] And so you can remotely
sort of indicate this [01:20:56] on the tablet, and then
the robot just does [01:20:59] everything in between. [01:21:00] - And it does everything,
all the coordinated movement [01:21:02] of all the different actuators
that includes the body [01:21:04] and the arm.
- Yeah, maintains its balance. [01:21:06] It walks itself, you know, into position [01:21:09] so it's within reach, and
the arm is in a position [01:21:12] where it can do the whole task. [01:21:14] So, it manages the whole body. [01:21:17] - So, how does one become
a big enough customer [01:21:20] to request features? [01:21:21] 'Cause I personally want a
robot that gets me a beer. [01:21:25] (Robert laughs) [01:21:26] I mean, that has to be,
like, one of the most, [01:21:29] I suppose, in the industrial setting, [01:21:30] that's a non-alcoholic beverage [01:21:35] of picking up objects and
bringing the objects to you. [01:21:38] - We love working with customers [01:21:39] who have challenging problems like this [01:21:41] and this one in particular because we felt [01:21:44] like what they were doing,
A, it was a safety feature. [01:21:47] B, we saw that the robot could do it [01:21:51] 'cause they teleoperated
it the first time. [01:21:53] Probably took 'em an hour to
do it the first time, right? [01:21:55] But the robot was clearly
capable, and we thought, [01:21:58] "Oh, this is a great
problem for us to work on [01:22:01] to figure out how to automate
a manipulation task." [01:22:03] And so, we took it on not because
we were gonna make a bunch [01:22:07] of money from it in selling
the robot back to them [01:22:09] but because it motivated
us to go solve what we saw [01:22:13] as the next logical step. [01:22:15] But many of our customers, in fact, [01:22:19] our bigger customers, typically ones [01:22:22] who are gonna run a utility, or a factory, [01:22:23] or something like that, we
take that kind of direction [01:22:27] from them, especially
if they're gonna buy 10, [01:22:29] or 20, or 30 robots, and they say, [01:22:31] "I really need it to do
this," well, that's exactly [01:22:34] the right kind of problem
that we wanna be working on. [01:22:35] - Mm-hmm.
- Yeah, and so- [01:22:37] - Note to self, "Buy 10 Spots,
(Robert laughs) [01:22:40] and aggressively push
for beer manipulation." [01:22:43] (Robert laughs) [01:22:45] I think it's fair to say
it's notoriously difficult [01:22:47] to make a lot of money
as a robotics company. [01:22:50] How can you make money
as a robotics company? [01:22:54] Can you speak to that? [01:22:55] It seems that a lot of
robotics companies fail. [01:23:00] It's difficult to build robots. [01:23:02] It's difficult to build
robots at a low enough cost [01:23:06] where customers, even in
the industrial setting, want [01:23:08] to purchase them, and it's
difficult to build robots [01:23:10] that are useful, sufficiently useful. [01:23:13] - [Robert] Yeah.
- So, what can you speak to? [01:23:14] And Boston Dynamics has been
successful for many years [01:23:18] of finding a way to make money. [01:23:21] - Well, in the early
days, of course, you know, [01:23:23] the money we made was from
doing contract R&D work, [01:23:26] and we made money, but you
know, we weren't growing, [01:23:29] and we weren't selling a product. [01:23:31] And then, we went through several owners [01:23:34] who, you know, had a vision
of not only developing [01:23:39] advanced technology, but
eventually developing products. [01:23:42] And so, both, you know,
Google, and SoftBank, [01:23:45] and now Hyundai, you know, had
that vision and were willing [01:23:49] to, you know, provide that investment. [01:23:55] Now, our discipline is that we
need to go find applications [01:23:59] that are broad enough that
you could imagine selling [01:24:02] thousands of robots
because it doesn't work [01:24:04] if you don't sell thousands or
tens of thousands of robots. [01:24:07] If you only sell hundreds,
you will commercially fail. [01:24:10] And that's where most [01:24:11] of the small robot companies have died. [01:24:18] And that's a challenge because, you know, [01:24:20] A, you need to field the robots. [01:24:22] They need to start to become
reliable, and as we've said, [01:24:25] that takes time and
investment to get there. [01:24:29] And so, it really does take [01:24:30] visionary investment to get there. [01:24:32] But we believe that we
are going to make money [01:24:36] in this industrial monitoring space [01:24:40] because, you know, if a chip fab, [01:24:45] if the line goes down [01:24:46] because a vacuum pump failed someplace, [01:24:49] that can be a very expensive process. [01:24:51] It can be a million dollars
a day in lost production, [01:24:54] maybe you have to throw away some [01:24:55] of the product along the
way, and so the robot, [01:24:59] if you can prevent that [01:25:00] by inspecting the
factory every single day,