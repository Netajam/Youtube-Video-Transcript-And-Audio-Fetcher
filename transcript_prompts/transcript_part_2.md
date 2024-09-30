## Prompt Instruction
Please summarize the following parts of this transcript:

## Chapters Included
36:53 - DARPA Robotics Challenge, 51:13 - BigDog robot

## Transcript
[00:29:22] - That tool bag, you know-
- Tool bag. [00:29:24] - had loose stuff in
it, so it managed that. [00:29:28] There are harder things
that we haven't done yet. [00:29:30] You know, we could have
had a big jointed thing [00:29:32] or, I don't know, a bunch
of loose wire or rope. [00:29:35] - What about carrying another robot? [00:29:36] How 'bout that? (laughing) [00:29:39] - Yeah, we haven't done that yet. [00:29:41] - [Lex] Carry Spot. [00:29:41] - I guess we did a little bit of a, [00:29:43] we did a little skit around Christmas [00:29:46] where we had two Spots
holding up another Spot [00:29:48] that was trying to put,
you know, a bow on a tree. [00:29:51] So, I guess we're doing that
in a small way. (laughing) [00:29:54] - Okay, that's pretty good. [00:29:56] Let me ask the all-important question. [00:29:58] Do you know how much Atlas can curl? [00:30:00] (Robert laughing drown out Lex speaking) [00:30:03] (Lex laughs) [00:30:04] I mean, you know, for us
humans, that's really one [00:30:08] of the most fundamental questions [00:30:09] you can ask another human being, [00:30:11] curl, bench, et cetera.
(Robert laughs) [00:30:14] - It probably can't curl
as much as we can yet, [00:30:17] but a metric that I
think is interesting is, [00:30:21] you know, another way of
looking at that strength is, [00:30:23] you know, the box jump. [00:30:25] So, how high of a box can you jump onto? [00:30:29] - [Lex] Question. [00:30:30] - And Atlas, I don't
know the exact height. [00:30:33] It was probably a meter
high or something like that. [00:30:34] It was a pretty pretty tall
jump that Atlas was able [00:30:37] to manage when we last tried to do this. [00:30:40] And I have video of my
chief technical officer [00:30:44] doing the same jump, and he
really struggled, you know, [00:30:46] to get-
- Oh, the human? [00:30:48] - The human getting all
the way on top of this box. [00:30:50] But then, you know,
Atlas was able to do it. [00:30:54] We're now thinking about the
next generation of Atlas, [00:30:56] and we're probably gonna be in the realm [00:30:58] of a person can't do it, you
know, with the next generation. [00:31:02] The robots, the actuators
are gonna get stronger [00:31:05] where it really is the
case that at least some [00:31:07] of these joints, some of these
motions will be stronger. [00:31:10] - And to understand how high it can jump, [00:31:11] you probably had to do
quite a bit of testing. [00:31:14] - Oh, yeah, and there's
lots of videos of it trying [00:31:16] and failing, and you know,
that's all, you know, [00:31:19] we don't always release those videos, [00:31:20] but they're a lot of
fun to look at. (laughs) [00:31:23] - So, we'll talk a little bit about that. [00:31:26] But can you talk to the jumping? [00:31:28] 'Cause you talked about the walking, [00:31:30] and it took a long time, many, many years [00:31:32] to get the walking to be natural, [00:31:34] but there's also really natural-looking, [00:31:38] robust, resilient jumping. [00:31:40] How hard is it to do the jumping? [00:31:43] - Well, again, this stuff
has really evolved rapidly [00:31:45] in the last few years. [00:31:46] You know, the first time we
did a somersault, you know, [00:31:49] there was a lot of kind
of manual iteration. [00:31:53] What is the trajectory? [00:31:54] You know, how hard do you throw? [00:31:55] In fact, in these early days, [00:32:00] when I'd see early experiments
that the team was doing, [00:32:03] I might make suggestions about
how to change the technique, [00:32:06] again, kind of borrowing
from my own intuition [00:32:09] about how backflips work. [00:32:12] But frankly they don't need that anymore. [00:32:13] So, in the early days,
you had to iterate kind [00:32:16] of in almost a manual way trying [00:32:19] to change these trajectories
of the arms or the legs [00:32:23] to try to get, you know, a
successful backflip to happen. [00:32:27] But more recently, we're running [00:32:29] these model-predictive control techniques [00:32:34] where the robot essentially
can think in advance [00:32:38] for the next second or two
about how its motion is going [00:32:42] to transpire, and you can, you know, solve [00:32:44] for optimal trajectories
to get from A to B. [00:32:47] So, this is happening in
a much more natural way, [00:32:50] and we're really seeing
an acceleration happen [00:32:53] in the development of these behaviors, [00:32:55] again, partly due to these
optimization techniques, [00:33:00] sometimes learning techniques, [00:33:03] so it's hard in that there's a
lot of mathematics behind it, [00:33:10] but we're figuring that out. [00:33:12] - So, you can do
model-predictive control for, [00:33:16] I mean, I don't even
understand what that looks like [00:33:18] when the entire robot is in the air [00:33:20] flying and doing a back (laughs). [00:33:22] - Yeah, well-
- I mean. (laughs) [00:33:25] - But that's the cool part, right? [00:33:26] So, you know, the physics, [00:33:28] we can calculate physics
pretty well using, you know, [00:33:30] Newton's laws about how it's
going to evolve over time [00:33:34] and you know, the sick trick,
which was a front somersault [00:33:38] with a half twist is
a good example, right? [00:33:42] You saw the robot on various
versions of that trick. [00:33:46] I've seen it land in
different configurations, [00:33:49] and it still manages to stabilize
itself, and so, you know, [00:33:53] what this model-predictive
control means is, again, [00:33:57] in real time, the robot is
projecting ahead, you know, [00:34:01] a second into the future and
sort of exploring options. [00:34:04] And if I move my arm a
little bit more this way, [00:34:06] how is that gonna affect the outcome? [00:34:08] And so, it can do these
calculations, many of them, [00:34:11] you know, and basically solve [00:34:14] for where, you know, given where I am now, [00:34:16] maybe I took off a little bit screwy [00:34:18] from how I had planned, I can adjust. [00:34:21] - [Lex] So, you're adjusting in the air [00:34:22] for the landing.
- Adjust on the fly. [00:34:24] So, the model-predictive
control lets you adjust [00:34:26] on the fly, and of course, I think this is [00:34:28] what, you know, people adapt as well. [00:34:31] When we do it, even a gymnastics trick, [00:34:34] we try to set it up so it's
close to the same every time. [00:34:38] But we figured out how to do
some adjustment on the fly, [00:34:40] and now we're starting to figure out [00:34:42] that the robots can do
this adjustment on the fly [00:34:44] as well using these techniques. [00:34:46] - In the air. [00:34:49] I mean, it just feels, [00:34:50] from a robotics perspective, just surreal. [00:34:53] - You talked about underactuated, right? [00:34:55] - [Lex] Yes.
- So, when you're- [00:34:56] - That's totally true.
- When you're in the air, [00:34:59] there's some things you
can't change, right? [00:35:00] You can't change the momentum
while it's in the air [00:35:02] 'cause you can't apply an
external force, a torque, [00:35:05] and so the momentum isn't gonna change. [00:35:07] So, how do you work within the constraint [00:35:09] of that fixed momentum to
still get from A to B (laughs) [00:35:13] where you wanna be? [00:35:14] - That's really (laughing) underactuated. [00:35:16] (Robert laughs) [00:35:17] You're in the air. [00:35:18] I mean, you become a drone
for a brief moment in time. [00:35:21] No, you're not even a (laughing)
drone 'cause you can't- [00:35:23] - [Robert] Can't hover. [00:35:24] - You can't hover. [00:35:25] You can't.
- You're gonna impact soon. [00:35:27] Be ready. (laughs)
- Yeah. [00:35:28] Have you considered like
a hover type thing or no? [00:35:31] No?
- No. [00:35:32] - It's too much weight?
- No. [00:35:33] (Lex laughing) [00:35:33] - I mean, it's just
incredible and just even [00:35:37] to have the guts to try a
backflip with such a large body. [00:35:42] That's wild. [00:35:43] (Robert laughs) [00:35:44] But, like how- [00:35:44] - We definitely broke a
few robots trying that. [00:35:46] - [Lex] (laughing) Yeah. [00:35:47] (Robert laughs) [00:35:48] - But that's where the
build it, break it, fix it, [00:35:49] you know, strategy comes in. [00:35:51] You gotta be willing to break. [00:35:52] And what ends up happening is [00:35:55] by breaking the robot repeatedly,
you find the weak points, [00:35:58] and then you end up redesigning it [00:35:59] so it doesn't break so easily
next time, you know. (laughs) [00:36:02] - Through the breaking
process you learn a lot, [00:36:05] like, a lot of lessons,
and you keep improving [00:36:07] not just how to make the backflip work, [00:36:09] but everything just-
- Yeah. [00:36:10] And how to build the machine better. [00:36:11] - Yeah.
- Yeah. [00:36:13] - I mean, is there something
about just the guts [00:36:15] to come up with an idea
of saying, "You know what? [00:36:19] Let's try (laughing) to
make it to a backflip"? [00:36:21] - Well, I think the
courage to do a backflip [00:36:24] in the first place and
to not worry too much [00:36:26] about the ridicule of somebody saying, [00:36:28] "Why the heck are you doing
backflips with robots?" [00:36:30] - [Lex] Sure. [00:36:31] - Because a lot of people
have asked that, you know. [00:36:33] (Lex laughs) [00:36:34] (laughing) "Why are you doing this?" [00:36:35] - Why go to the moon [00:36:36] (Robert laughs) [00:36:37] in this decade and do
the other things, JFK? [00:36:40] (Robert laughs) [00:36:41] Not because it's easy, because it's hard. [00:36:43] - [Robert] Yeah, exactly. (laughs) [00:36:45] (Lex laughs) [00:36:46] - Don't ask questions. [00:36:48] Okay, so the jumping, I mean, [00:36:50] there's a lot of incredible stuff. [00:36:51] If we can just rewind a little bit [00:36:53] to the DARPA Robotics
Challenge in 2015, I think, [00:36:57] which was, for people who aren't familiar [00:37:00] with the DARPA challenges, it was first [00:37:04] with autonomous vehicles,
and there's a lot [00:37:06] of interesting challenges around that. [00:37:07] And the DARPA Robotics Challenge was [00:37:09] when humanoid robots were
tasked to do all kinds [00:37:15] of, you know, manipulation, walking- [00:37:21] - Driving a vehicle.
- driving a car, [00:37:22] all these kinds of challenges
with, if I remember correctly, [00:37:26] sort of some slight capability
to communicate with humans, [00:37:31] but the communication was very poor. [00:37:34] So, basically it has to be
almost entirely autonomous. [00:37:37] - It could have periods [00:37:38] where the communication
was entirely interrupted, [00:37:40] and the robot had to be able to proceed. [00:37:42] - [Lex] Yeah. [00:37:43] - But you could provide
some high-level guidance [00:37:44] to the robot, basically
low-bandwidth communications- [00:37:48] - Yeah
- to steer it. [00:37:49] - I watched that challenge
with kind of tears in my eyes [00:37:53] eating popcorn with-
- Us, too. [00:37:55] (both laughing) [00:37:57] - But I wasn't personally
losing, you know, [00:38:00] hundreds of thousands, millions of dollars [00:38:02] and many years of incredible, hard work [00:38:05] by some of the most brilliant
roboticists in the world. [00:38:08] So, that was why the tragic, [00:38:10] that's why tears came.
(Robert laughs) [00:38:11] So, anyway, just looking
back to that time, [00:38:15] what have you learned
from that experience? [00:38:18] And maybe if you could
describe what it was [00:38:20] sort of the setup for
people who haven't seen it. [00:38:23] - Well, so there was a contest [00:38:24] where a bunch of different
robots were asked [00:38:28] to do a series of tasks, some
of those that you mentioned, [00:38:31] drive a vehicle, get out, open a door, [00:38:34] go identify a valve, shut a valve, [00:38:37] use a tool to maybe
cut a hole in a surface [00:38:43] and then crawl over some stairs [00:38:45] and maybe some rough terrain. [00:38:47] So, the idea was have
a general-purpose robot [00:38:53] that could do lots of different things, [00:38:57] had to be mobility, and
manipulation, on-board perception. [00:39:01] And there was a contest, [00:39:03] which DARPA likes at the
time, was running sort [00:39:07] of follow-on to the grand challenge, [00:39:10] which was, "Let's try to
push vehicle autonomy along." [00:39:14] Right? [00:39:15] They encouraged people
to build autonomous cars. [00:39:18] So, they were trying to basically
push an industry forward. [00:39:25] Our role in this was to build a humanoid. [00:39:28] At the time, it was our sort [00:39:30] of first-generation Atlas robot, [00:39:33] and we built maybe 10 of them, [00:39:37] I don't remember the exact number. [00:39:39] And DARPA distributed those
to various teams that sort [00:39:45] of won a contest, showed that
they could, you know, program [00:39:50] these robots and then use them [00:39:51] to compete against each other, [00:39:53] and then other robots
were introduced as well. [00:39:55] Some teams built their own robots. [00:39:56] Carnegie Mellon, for example,
built their own robot. [00:40:01] And all these robots competed
to see who could sort of get [00:40:04] through this maze the fastest. [00:40:07] And again, I think the purpose was to kind [00:40:10] of push the whole industry forward. [00:40:13] We provided the robot and
some baseline software, [00:40:16] but we didn't actually
compete as a participant [00:40:20] where we were trying to,
you know, drive the robot [00:40:24] through this maze. [00:40:25] We were just trying to
support the other teams. [00:40:28] It was humbling because
it was really a hard task. [00:40:32] And honestly, the tears were [00:40:34] because, mostly, the robots
didn't do it. (laughs) [00:40:35] You know, they fell down,
you know, repeatedly. [00:40:41] It was hard to get through this contest. [00:40:44] Some did, and you know,
they were rewarded and won. [00:40:48] But it was humbling
because of just how hard, [00:40:50] these tasks weren't all that hard. [00:40:51] A person could have done it very easily, [00:40:54] but it was really hard to get
the robots to do it, you know. [00:40:56] And the-
- The general nature of it, [00:40:59] the variety of it. [00:41:00] - [Robert] The variety. [00:41:01] - And also, I don't know
if the tasks were (sighs) [00:41:06] sort of the task in
themselves help us understand [00:41:10] what is difficult and what is not. [00:41:12] I don't know if that was obvious [00:41:13] before the contest was designed, [00:41:15] so you kind of tried to figure that out. [00:41:17] And I think Atlas is really
a general robot platform, [00:41:22] and it's perhaps not best
suited for the specific tasks [00:41:26] of that contest, like just for example, [00:41:29] probably the hardest task is
not the driving of the car [00:41:33] but getting in and out of the car. [00:41:35] (Robert laughs) [00:41:35] And Atlas probably is,
you know, if you were [00:41:38] to design a robot that can
get into the car easily [00:41:41] and get out easily, you
probably would not make Atlas [00:41:44] that particular car. [00:41:45] - Yeah, the robot was a little bit big- [00:41:47] - Yeah.
- to get in [00:41:48] and out of that car, right? [00:41:49] - [Lex] It doesn't fit, yeah. [00:41:50] - This is the curse of
a general-purpose robot, [00:41:53] that they're not perfect at any one thing, [00:41:56] but they might be able to
do a wide variety of things. [00:41:59] And that is the goal
at the end of the day. [00:42:04] You know, I think we all wanna
build general-purpose robots [00:42:08] that can be used for lots
of different activities, [00:42:11] but it's hard, and the wisdom [00:42:15] in building successful robots
up until this point have been, [00:42:19] "Go build a robot for a specific task, [00:42:22] and it'll do it very well." [00:42:24] And as long as you
control that environment, [00:42:26] it'll operate perfectly,
but robots need to be able [00:42:30] to deal with uncertainty. [00:42:31] If they're gonna be useful
to us in the future, [00:42:34] they need to be able to deal
with unexpected situations. [00:42:38] And that's sort of the goal [00:42:39] of a general-purpose
or multipurpose robot. [00:42:42] And that's just darn hard. [00:42:44] And so, yeah, there was these
curious little failures. [00:42:46] Like, I remember a robot, you know, [00:42:51] the first time you start
to try to push on the world [00:42:54] with a robot, you forget
that the world pushes back [00:42:58] and will push you over (laughs)
if you're not ready for it. [00:43:02] And the robot, you know,
reached to grab the door handle. [00:43:05] I think it missed the
grasp of the door handle, [00:43:08] was expecting that its hand
was on the door handle, [00:43:10] and so when it tried to turn the knob, [00:43:12] it just threw itself over. [00:43:14] It didn't realize, "Oh, I
had missed the door handle. [00:43:18] I was expecting a force
back from the door. [00:43:21] It wasn't there, and
then I lost my balance." [00:43:23] And so, these little simple things [00:43:25] that you and I would
take totally for granted [00:43:27] and deal with, (laughs)
the robots don't know [00:43:30] how to deal with yet, and
so you have to start to deal [00:43:32] with all of those circumstances. (laughs) [00:43:35] - Well, I think a lot
of us experience this [00:43:39] even when sober but drunk, too. [00:43:42] Sort of, you pick up a
thing and expect it to be, [00:43:45] what is it, heavy, and
it turns out to be light. [00:43:49] - [Robert] Yeah, and then, "Whoa." [00:43:49] - Oh, yeah, and then, and I'm
sure if your depth perception [00:43:53] for whatever reason is screwed up, [00:43:56] if you're drunk or some other reason, [00:43:58] and then you think you're
putting your hand on the table, [00:44:01] and you miss it, I mean it's
the same kind of situation. [00:44:03] - [Robert] Yeah. [00:44:04] - But there's a-
- Which is why you need [00:44:06] to be able to predict forward
just a little bit, and so [00:44:09] that's where this model-predictive
control stuff comes in. [00:44:11] Predict forward what you
think's gonna happen, [00:44:15] and if that does happen,
you're in good shape. [00:44:16] If something else happens, [00:44:17] you better start predicting again. [00:44:19] - So, like, regenerate a plan.
(Robert laughs) [00:44:22] - [Robert] Yeah. [00:44:24] - I mean, that also requires
a very fast feedback loop [00:44:30] of updating what your prediction, [00:44:33] how it matches to the actual real world. [00:44:36] - [Robert] Yeah, those things
have to run pretty quickly. [00:44:38] - What's the challenge of
running things pretty quickly, [00:44:40] 1,000 hertz, of acting
and sensing quickly? [00:44:47] - You know, there's a few
different layers of that. [00:44:50] At the lowest level, you
like to run things typically [00:44:53] at around 1,000 hertz,
which means that, you know, [00:44:55] at each joint of the robot,
you're measuring position [00:44:59] or force and then trying
to control your actuator, [00:45:02] whether it's a hydraulic
or electric motor trying [00:45:05] to control the force coming
out of that actuator. [00:45:07] And you wanna do that really fast, [00:45:10] something like 1,000 hertz,
and that means you can't have [00:45:13] too much calculation
going on at that joint. [00:45:17] But that's pretty manageable these days, [00:45:18] and it's fairly common. [00:45:20] And then, there's another layer [00:45:22] that you're probably
calculating, you know, [00:45:24] maybe at 100 hertz, maybe 10 times slower, [00:45:27] which is now starting to look
at the overall body motion [00:45:31] and thinking about the
larger physics of the robot. [00:45:37] And then, there's yet another
loop that's probably happening [00:45:40] a little bit slower, which
is where you start to bring, [00:45:42] you know, your perception in, your vision, [00:45:45] and things like that, and
so you need to run all [00:45:48] of these loops sort of simultaneously. [00:45:50] You do have to manage your computer time [00:45:54] so that you can squeeze in
all the calculations you need [00:45:57] in real time in a very consistent way. [00:46:01] And the amount of calculation
we can do is increasing [00:46:06] as computers get better,
which means we can start [00:46:08] to do more sophisticated calculations. [00:46:10] I can have a more complex model
doing my forward prediction, [00:46:16] and that might allow me to
do even better predictions [00:46:19] as I get better and better. [00:46:21] And it used to be, again,
you know, 10 years ago, [00:46:26] we had to have pretty simple
models that we were running, [00:46:30] you know, at those fast rates
'cause the computers weren't [00:46:33] as capable about calculating forward [00:46:36] with a sophisticated model,
but as computation gets better, [00:46:41] we can do more of that. [00:46:42] - What about the actual pipeline
of software engineering, [00:46:46] how easy it is to keep updating Atlas, [00:46:48] like, do continuous development on it? [00:46:51] So, how many computers are on there? [00:46:54] Is there a nice pipeline? [00:46:56] - It's an important part of
building a team around it, [00:47:00] which means, you know, you need
to also have software tools, [00:47:04] simulation tools, you know, [00:47:06] so we have always made strong use [00:47:11] of physics-based
simulation tools to do some [00:47:15] of this calculation, basically
test it in simulation [00:47:19] before you put it on the robot. [00:47:21] But you also want the same
code that you're running [00:47:23] in simulation to be the
same code you're running [00:47:25] on the hardware, and so
even getting to the point [00:47:28] where it was the same code
going from one to the other, [00:47:32] we probably didn't really get that working [00:47:34] until, you know, several years ago. [00:47:37] But you know, that was
a bit of a milestone. [00:47:39] And so, you wanna certainly
work these pipelines [00:47:42] so that you can make
it as easy as possible [00:47:44] and have a bunch of people
working in parallel. [00:47:47] You know, we only have, you
know, four of the Atlas robots, [00:47:51] the modern Atlas robots at
the company, and you know, [00:47:54] we probably have, you
know, 40 developers there [00:47:57] all trying to gain access to it. [00:47:59] And so, you need to share resources [00:48:02] and use some of the software pipeline. [00:48:04] - Well, that's a really
exciting step to be able to run [00:48:06] the exact same code in simulation
as on the actual robot. [00:48:10] How hard is it to do [00:48:14] a realistic simulation, [00:48:16] physics-based simulation
of Atlas such that, [00:48:20] I mean, the dream is like,
if it works in simulation, [00:48:23] it works perfectly in reality.
(Robert laughs) [00:48:25] How hard is it to sort of keep
working on closing that gap? [00:48:28] - The root of some of our
physics-based simulation tools [00:48:31] really started at MIT, and we built [00:48:36] some good physics-based
modeling tools there. [00:48:39] The early days of the
company, we were trying [00:48:41] to develop those tools
as a commercial product, [00:48:43] so we continued to develop them. [00:48:45] It wasn't a particularly
successful commercial product, [00:48:48] but we ended up [00:48:49] with some nice physics-based
simulation tools [00:48:50] so that, when we started
doing legged robotics again, [00:48:52] we had a really nice tool to work with. [00:48:55] And the things we paid
attention to were things [00:48:58] that weren't necessarily handled very well [00:49:00] in the commercial tools you
could buy off the shelf, [00:49:03] like interaction with the
world, like foot-ground contact. [00:49:07] And so, trying to model
those contact events well [00:49:13] in a way that captured the important parts [00:49:16] of the interaction was a
really important element [00:49:21] to get right and to also do in a way [00:49:23] that was computationally
feasible and could run fast [00:49:27] 'cause if your simulation
runs too slow, you know, [00:49:31] then your developers are
sitting around waiting for stuff [00:49:33] to run and compile, and so it's always [00:49:35] about efficient, fast operation as well. [00:49:40] So, that's been a big part of it. [00:49:41] You know, I think developing
those tools in parallel [00:49:44] to the development of
the platform and trying [00:49:47] to scale them has really
been essential, I'd say, [00:49:50] to us being able to
assemble a team of people [00:49:53] that could do this. [00:49:55] - Yeah, how to simulate contact, period, [00:49:57] so foot-ground contact but
sort of for manipulation [00:50:02] because don't you want to
model all kinds of surfaces? [00:50:06] - Yeah. [00:50:07] So, it will be even more
complex with manipulation [00:50:09] 'cause there's a lot
more going on. (laughs) [00:50:11] - Yeah.
- You know. [00:50:12] And you need to capture, I don't know, [00:50:14] things slipping and moving,
you know, in your hand. [00:50:20] It's a level of complexity
that I think goes [00:50:23] above foot-ground contact [00:50:26] when you really start doing
dextrous manipulation. [00:50:29] So, there's challenges ahead still. [00:50:31] - So, how far are we away
from me being able to walk [00:50:34] with Atlas in the sand along the beach [00:50:37] (Robert laughs) [00:50:38] and us both drinking a beer? [00:50:40] (Robert laughing) [00:50:41] - [Robert] Well, I- [00:50:42] - Sip it out of a can, out of a can. [00:50:43] - Maybe Atlas could spill his beer [00:50:45] 'cause he's got nowhere
to put it. (laughing) [00:50:48] Atlas could walk on the sand. [00:50:50] - So, can it?
- Yeah, yeah. [00:50:52] Yeah, I mean, you know,
have we really had him [00:50:54] out on the beach? [00:50:55] You know, we take them outside often, [00:50:57] you know, rocks, hills,
that sort of thing, [00:50:59] even just around our lab in Waltham. [00:51:02] We probably haven't been
on the sand, but I'm- [00:51:04] - So, soft surfaces, normally?
- I don't doubt [00:51:06] that we could deal with it. [00:51:08] We might have to spend
a little bit of time [00:51:10] to sort of make that work. [00:51:14] We had to take BigDog
to Thailand years ago, [00:51:20] and we did this great video [00:51:22] of the robot walking in the sand, [00:51:25] walking into the ocean up
to, I don't know, its belly [00:51:29] or something like that and
then turning around and walking [00:51:31] out all while playing-
- Oh, that's- [00:51:32] - [Robert] some cool beach music. [00:51:34] - Yeah.
- Great show, [00:51:35] but then, you know, we didn't
really clean the robot off, [00:51:37] and the saltwater was really
hard on it, so you know, [00:51:40] we put it in a box, shipped it back. [00:51:42] By the time it came back, [00:51:43] we had some problems
(laughing) with corrosion. [00:51:46] - It's the salt water. [00:51:47] It's not like-
- Salt tough (laughs). [00:51:49] - It's not, like, sand getting [00:51:50] into the components or
something like this. [00:51:51] - [Robert] Yeah, yeah.
- But I'm sure, [00:51:53] if this is a big priority,
you can make it like- [00:51:55] - Right.
- waterproof it [00:51:56] or something.
- Right, right. [00:51:57] That just wasn't our goal at the time. [00:51:59] - Well, it's a personal goal of mine [00:52:01] to walk along,
(Robert laughs) [00:52:02] walk along the beach, but
it's a human problem, too. [00:52:04] You get sand everywhere. [00:52:05] It's just a giant mess. [00:52:07] (Robert laughs) [00:52:08] So, soft surfaces are okay. [00:52:10] So, I mean, can we just linger
on the robotics challenge? [00:52:15] There's a pile of, like,
rubble they had to walk over. [00:52:21] How difficult is that task? [00:52:23] - In the early days of developing BigDog, [00:52:26] the loose rock was the epitome
of the hard walking surface [00:52:30] because you stepped down, [00:52:32] and you had these little
point feet on the robot, [00:52:35] and the rock can roll,
and you have to deal [00:52:39] with that last-minute, you know, change [00:52:41] in your foot placement. [00:52:43] - Yeah, so you step on the
thing, and that thing responds [00:52:46] to you stepping on it. [00:52:47] - Yeah, and it moves where
your point of support is. [00:52:50] And so, that became kinda
the essence of the test. [00:52:55] And so, that was the
beginning of us starting [00:52:57] to build rock piles in our parking lots, [00:53:01] and we would actually
build boxes full of rocks [00:53:04] and bring 'em into the
lab, and then we would have [00:53:07] the robots walking across
these boxes of rocks [00:53:09] because that became the essential test. [00:53:12] - So, you mentioned BigDog. [00:53:14] Can we maybe take a stroll [00:53:16] through the history of Boston Dynamics? [00:53:18] So, what and who is BigDog? [00:53:21] By the way, is who, [00:53:23] (Robert laughs) [00:53:24] do you try not to
anthropomorphize the robots? [00:53:30] Do you try to remember that they're, [00:53:31] this is like the division I have [00:53:32] 'cause, for me, it's impossible. [00:53:35] For me, there's a magic to
the being that is a robot. [00:53:37] It is not human, but it is, [00:53:41] the same magic that a living
being has when it moves [00:53:46] about the world is there in the robot. [00:53:48] So, I don't know what question I'm asking, [00:53:51] but should I say what or who I guess? [00:53:54] Who is BigDog? [00:53:55] What is BigDog?
(Robert laughs) [00:53:57] - Well, I'll say to
address the meta question, [00:54:00] we don't try to draw hard
lines around it being an it, [00:54:03] or a him, or a her. [00:54:07] It's okay, right? [00:54:09] I think part of the magic of
these kinds of machines is [00:54:13] by nature of their organic
movement, of their dynamics, [00:54:18] we tend to want to identify with them. [00:54:22] We tend to look at them and
sort of attribute maybe feeling [00:54:27] to that because we've only seen things [00:54:29] that move like this that were alive. [00:54:32] And so, this is an opportunity. [00:54:35] It means that you could
have feelings for a machine, [00:54:41] and you know, people have
feelings for their cars. [00:54:43] You know, they get attracted
to 'em, attached to them. [00:54:46] So, that's inherently,
could be a good thing [00:54:49] as long as we manage
what that interaction is. [00:54:52] So, we don't put strong
boundaries around this [00:54:56] and ultimately think it's a benefit, [00:54:58] but it's also, can be a bit of a curse [00:55:01] because I think people
look at these machines, [00:55:04] and they attribute a level of intelligence [00:55:06] that the machines don't have. [00:55:08] Why? [00:55:09] Because, again, they've
seen things move like this [00:55:11] that we're living beings,
which are intelligent, [00:55:16] and so they wanna attribute
intelligence to the robots [00:55:18] that isn't appropriate yet, [00:55:20] even though they move
like an intelligent being. [00:55:22] - But you try to acknowledge [00:55:24] that the anthropomorphization
is there and try [00:55:27] to, first of all,
acknowledge that it's there. [00:55:31] - And have a little fun with it. [00:55:32] - And have little fun.
- You know, [00:55:33] our most recent video,
it's just kind of fun, [00:55:36] you know, to look at the robot. [00:55:40] We started off the video
with Atlas kind of looking [00:55:45] around for where the bag of tools was [00:55:48] 'cause the guy up on the scaffolding says, [00:55:49] "Send me some tools." [00:55:51] Atlas has to kinda look
around and see where they are. [00:55:54] And there's a little
personality there that is fun. [00:55:58] It's entertaining. [00:55:58] It makes our jobs interesting [00:56:00] and I think in the long
run can enhance interaction [00:56:03] between humans and robots in a way [00:56:06] that isn't available to machines
that don't move that way. [00:56:09] - This is something to me
personally is very interesting. [00:56:13] I happen to have a lot of legged robots. [00:56:16] (both laughing) [00:56:18] I hope to have a lot of
Spots in my possession. [00:56:22] I'm interested in celebrating robotics [00:56:24] and celebrating companies, companies [00:56:27] that do incredible stuff
like Boston Dynamics. [00:56:32] You know, I'm a little crazy,
and you say you don't want to, [00:56:36] you want to align, you
wanna help the company [00:56:39] 'cause I ultimately want a company [00:56:42] like Boston Dynamics to succeed. [00:56:43] And part of that we'll
talk about, you know, [00:56:45] success kind of requires making money.