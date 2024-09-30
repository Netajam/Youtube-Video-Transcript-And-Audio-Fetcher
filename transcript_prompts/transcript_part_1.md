## Prompt Instruction
Please summarize the following parts of this transcript:

## Chapters Included
0:00 - Introduction, 2:57 - Early days of Boston Dynamics, 11:18 - Simplifying robots, 15:16 - Art and science of robotics, 19:59 - Atlas humanoid robot

## Transcript
[00:00:00] - And so our goal was
a natural-looking gait. [00:00:03] It was surprisingly hard
to get that to work. [00:00:07] But we did build an early machine. [00:00:10] We called it PETMAN prototype. [00:00:12] It was the prototype
before the PETMAN robot, [00:00:16] and it had a really nice-looking gait [00:00:20] where, you know, it
would stick the leg out. [00:00:23] It would do heel strike first
before it rolled onto the toe, [00:00:25] so you didn't land with a flat foot. [00:00:27] You extended your leg a
little bit, but even then, [00:00:31] it was hard to get the robot to walk [00:00:33] where, when you were walking, [00:00:34] that it fully extended its leg [00:00:37] and getting that all to work
well took such a long time. [00:00:42] In fact, I probably didn't really see [00:00:45] the nice, natural walking that I expected [00:00:48] out of our humanoids
until maybe last year. [00:00:51] And the team was developing
on our newer generation [00:00:54] of Atlas, you know, some new techniques [00:00:59] for developing a
walking-control algorithm. [00:01:01] And they got that
natural-looking motion as sort [00:01:04] of a byproduct of just a different process [00:01:07] they were applying to
developing the control. [00:01:11] So, that probably took 15
years, 10 to 15 years to sort [00:01:15] of get that from, you know, [00:01:17] the PETMAN prototype was probably in 2008, [00:01:20] and what was it, 2022, (laughs) last year [00:01:23] that I think I saw good walking on Atlas. [00:01:25] (dramatic music) [00:01:27] - The following is a
conversation with Robert Playter, [00:01:30] CEO of Boston Dynamics, a
legendary robotics company [00:01:35] that, over 30 years, has created
some of the most elegant, [00:01:39] dextrous, and simply
amazing robots ever built, [00:01:42] including the humanoid robot
Atlas and the robot dog Spot, [00:01:48] one or both of whom you've
probably seen on the Internet, [00:01:52] either dancing, doing
backflips, opening doors, [00:01:56] or throwing around heavy objects. [00:01:59] Robert has led both the development [00:02:02] of Boston Dynamics humanoid robots [00:02:03] and their physics-based
simulation software. [00:02:07] He has been with the company
from the very beginning, [00:02:10] including its roots at MIT, [00:02:12] where he received his PhD
in aeronautical engineering. [00:02:16] This was in 1994 at the
legendary MIT Leg Lab. [00:02:21] He wrote his PhD thesis
on robot gymnastics [00:02:25] as part of which he programmed
a bipedal robot to do [00:02:28] the world's first 3D robotic somersault. [00:02:32] Robert is a great engineer,
roboticist, and leader, [00:02:35] and Boston Dynamics, to
me as a roboticist, is [00:02:38] a truly inspiring company. [00:02:40] This conversation was a
big honor and pleasure, [00:02:43] and I hope to do a lot of great work [00:02:45] with these robots in the years to come. [00:02:47] This is the Lex Fridman podcast. [00:02:49] To support it, please
check out our sponsors [00:02:51] in the description. [00:02:53] And now, dear friends,
here's Robert Playter. [00:02:57] When did you first fall
in love with robotics? [00:03:01] (Lex laughs) [00:03:02] Let's start with love and robots. [00:03:04] - Well, love is relevant because I think [00:03:08] the fascination, the deep fascination is [00:03:10] really about movement, and
I was visiting MIT looking [00:03:16] for a place to get a PhD, [00:03:19] and I wanted to do some laboratory work. [00:03:21] And one of my professors in
the aero department said, [00:03:24] "Go see this guy Marc Raibert [00:03:26] down in the basement of the AI lab." [00:03:29] And so I walked down there and saw him. [00:03:31] He showed me his robots, [00:03:33] and he showed me this
robot doing a somersault. [00:03:36] (Lex laughs) [00:03:37] And I just immediately
went, "Whoa," you know. [00:03:40] - [Lex] Yeah. [00:03:41] - "Robots can do that?" [00:03:41] And because of my own
interest in gymnastics, [00:03:44] there was, like, this
immediate connection, [00:03:46] and, you know, I was
in an aeroastro degree [00:03:51] because, you know, flight and movement was [00:03:54] all so fascinating to me. [00:03:55] And then it turned out [00:03:56] that, you know, robotics
had this big challenge. [00:04:00] How do you balance? [00:04:01] How do you build a legged robot
that can really get around? [00:04:06] That was a fascination,
and it still exists today. [00:04:09] We're still working on
perfecting motion in robots. [00:04:13] - What about the elegance and the beauty [00:04:15] of the movement itself? [00:04:16] Is there something maybe
grounded in your appreciation [00:04:20] of movement from your gymnastics days? [00:04:26] Was there something you just
fundamentally appreciated [00:04:28] about the elegance and beauty of movement? [00:04:31] - You know, we had this concept [00:04:32] in gymnastics of letting your
body do what it wanted to do. [00:04:38] When you get really good at gymnastics, [00:04:43] part of what you're doing
is putting your body [00:04:45] into a position where the physics [00:04:47] and the body's inertia and
momentum will kinda push you [00:04:51] in the right direction in a
very natural and organic way. [00:04:54] And the thing that Marc
was doing, you know, [00:04:56] in the basement of that laboratory
was trying to figure out [00:05:00] how to build machines to take
advantage of those ideas. [00:05:03] How do you build something
so that the physics [00:05:05] of the machine just
kind of inherently wants [00:05:08] to do what it wants to do? [00:05:09] And he was building these springy
pogo-stick type, you know. [00:05:13] His first cut at legged
locomotion was a pogo stick [00:05:16] where it's bouncing, and
there's a spring mass system [00:05:20] that's oscillating, has its own sort [00:05:22] of natural frequency
there and sort of figuring [00:05:25] out how to augment those natural
physics with also intent. [00:05:30] How do you then control
that but not overpower it? [00:05:33] It's that coordination that I
think creates real potential. [00:05:37] We could call it beauty, you know. [00:05:38] You could call it, I don't know, synergy. [00:05:41] People have different words for it. [00:05:43] But I think that that was
inherent from the beginning. [00:05:46] That was clear to me that that's part [00:05:48] of what Marc was trying to do. [00:05:49] He asked me to do that
in my research work. [00:05:51] So, you know, that's where it got going. [00:05:54] - So, part of the thing that
I think I'm calling elegance [00:05:56] and beauty in this case, which was there, [00:05:58] even with the pogo stick
is maybe the efficiency, [00:06:01] so letting the body do
what it wants to do, [00:06:04] trying to discover the efficient movement. [00:06:06] - It's definitely more efficient. [00:06:08] It also becomes easier
to control in its own way [00:06:12] because the physics are solving
some of the problem itself. [00:06:15] It's not like you have to
do all this calculation [00:06:18] and overpower the physics. [00:06:19] The physics naturally, inherently want [00:06:21] to do the right thing. [00:06:23] There can even be, you
know, feedback mechanisms, [00:06:26] stabilizing mechanisms
that occur simply by virtue [00:06:31] of the physics of the body. [00:06:32] And it's, you know,
not all in the computer [00:06:36] or not even all in your
mind as a person (laughs). [00:06:39] And there's something
interesting in that melding. [00:06:43] - You were with Marc for
many, many, many years, [00:06:46] but you were there in
this kinda legendary space [00:06:49] of Leg Lab and MIT in
the basement (laughs). [00:06:53] All great things happen in the basement. [00:06:55] (Robert laughs) [00:06:57] Is there some memories from
that time that you have? [00:07:00] Because it's such cutting-edge work [00:07:06] in robotics and artificial intelligence. [00:07:09] - The memories, the distinctive
lessons, I would say [00:07:12] I learned in that time period [00:07:16] and that I think Marc was
a great teacher of was [00:07:20] it's okay to pursue your
interests, your curiosity, [00:07:24] do something because you love it. [00:07:27] You'll do it a lot better if you love it. [00:07:32] That is a lasting lesson
that I think we apply [00:07:36] at the company still and
really is a core value. [00:07:41] - So, the interesting thing is, [00:07:46] with people like Russ Tedrake and others, [00:07:50] like, the students that work [00:07:51] at those robotics labs are, like, some [00:07:53] of the happiest people I've ever met. [00:07:55] I don't know what that is. (laughs) [00:07:57] I meet a lot of PhD students. [00:07:58] A lot of them are kind of broken [00:08:00] (laughing) by the wear
and tear of the process, [00:08:03] but roboticists are, while
they work extremely hard [00:08:06] and work long hours, [00:08:11] there's a happiness there. [00:08:12] The only other group of people
I've met like that are people [00:08:14] that skydive a lot. [00:08:15] (both laughing) [00:08:17] For some reason, there's a
deep, fulfilling happiness maybe [00:08:19] from, like, a long period of struggle [00:08:22] to get a thing to work, and it works, [00:08:24] and there's a magic to it. [00:08:24] I don't know exactly 'cause
it's so fundamentally hands-on, [00:08:29] and you're bringing a thing to life. [00:08:30] I don't know what it
is, but they're happy. [00:08:34] - You know, our attrition at
the company is really low. [00:08:37] People come, and they love the pursuit. [00:08:40] And I think part of that is [00:08:41] that there's perhaps a
natural connection to it. [00:08:45] It's a little bit easier to
connect when you have a robot [00:08:47] that's moving around in the
world, and part of your goal is [00:08:50] to make it move around in the world. [00:08:52] You can identify with that. [00:08:55] This is one of the unique things [00:08:56] about the kinds of
robots we're building is [00:08:58] this physical interaction lets
you perhaps identify with it. [00:09:03] So, I think that is a source of happiness. [00:09:05] I don't think it's unique to robotics. [00:09:07] I think anybody also who is just pursuing [00:09:10] something they love, it's
easier to work hard at it [00:09:13] and be good at it, and not
everybody gets to find that. [00:09:19] I do feel lucky in that way. [00:09:21] And I think we're lucky as an organization [00:09:23] that we've been able to
build a business around this [00:09:27] and that keeps people engaged. [00:09:29] - So, if it's all right,
let's linger on Marc [00:09:31] for a little bit longer, Marc Raibert. [00:09:33] So, he's a legend. [00:09:36] He's a legendary engineer and roboticist. [00:09:39] What have you learned about
life, about robotics from Marc [00:09:42] through all the many years
you've worked with him? [00:09:45] - I think the most important
lesson, which was, you know, [00:09:48] have the courage of your convictions [00:09:49] and do what you think is interesting. [00:09:53] Be willing to try to find
big, big problems to go after. [00:09:59] And at the time, you
know, legged locomotion, [00:10:02] especially in a dynamic
machine, nobody had solved it. [00:10:06] And that felt like a
multi-decade problem to go after. [00:10:12] And so, you know, have the
courage to go after that [00:10:15] because you're interested. [00:10:17] Don't worry if it's gonna make money. [00:10:19] You know, that's been a theme. [00:10:21] That's really probably the
most important lesson I think [00:10:26] that I got from Marc. [00:10:28] - How crazy is the effort
of doing legged robotics [00:10:32] at that time, especially? [00:10:35] - You know, Marc got some
stuff to work starting [00:10:38] from simple ideas. [00:10:40] So, maybe the other,
another important idea [00:10:42] that has really become a
value of the company is [00:10:45] try to simplify a thing
to the core essence. [00:10:51] While, you know, Marc was
showing videos of animals running [00:10:54] across the Savannah or climbing mountains, [00:10:59] what he started with was a pogo stick [00:11:00] because he was trying to
reduce the problem to something [00:11:03] that was manageable, and
getting the pogo stick [00:11:06] to balance had in it
the fundamental problems [00:11:10] that, if we solved those, you
could eventually extrapolate [00:11:12] to something that galloped
like a horse, and so look [00:11:16] for those simplifying principles. [00:11:19] - How tough is the job
of simplifying a robot? [00:11:22] - So, I'd say, in the early
days, the thing that made [00:11:27] the researchers at Boston
Dynamics special is [00:11:30] that we worked on figuring out [00:11:33] what that central principle was [00:11:38] and then building software or machines [00:11:41] around that principle,
and that was not easy [00:11:43] in the early days. [00:11:44] And it took real expertise
in understanding the dynamics [00:11:50] of motion and feedback-control
principles, how to build, [00:11:57] you know, with the computers at the time, [00:11:58] how to build a feedback-control algorithm [00:12:00] that was simple enough that
it could run in real time [00:12:02] at 1,000 hertz and actually
get that machine to work. [00:12:08] And that was not something
everybody was doing, [00:12:10] you know, at that time. [00:12:12] Now, the world's changing now,
and I think the approaches [00:12:15] to controlling robots are going to change, [00:12:20] and they're going to become
more broadly available. [00:12:26] But at the time, there weren't many groups [00:12:28] who could really sort of
work at that principled level [00:12:32] with both the software and
make the hardware work. [00:12:37] And I'll say one other thing
about you were sort of talking [00:12:40] about what are the special things. [00:12:41] The other thing was it's good
to break stuff, you know. [00:12:47] You know, use the robots,
break them, repair them, [00:12:53] you know, fix and repeat,
(laughs) test, fix, and repeat. [00:12:57] And that's also a core
principle that has become part [00:13:00] of the company, and it lets
you be fearless in your work. [00:13:05] Too often, if you are working
with a very expensive robot, [00:13:09] maybe one that you
bought from somebody else [00:13:11] or that you don't know how to fix, [00:13:12] then you treat it with kid gloves, [00:13:15] and you can't actually make progress. [00:13:17] You have to be able to break something. [00:13:19] And so, I think that's
been a principle as well. [00:13:22] - So, just to linger on
that, psychologically, [00:13:24] how do you deal with that? [00:13:25] 'Cause I remember I built a RC car. [00:13:33] It had some custom stuff
like a computer on it [00:13:35] and all that kind of stuff, cameras [00:13:37] and because I didn't sleep much, [00:13:41] the code I wrote had an issue
where it didn't stop the car, [00:13:44] and the car got confused and at full speed [00:13:47] at, like, 20, 25 miles an
hour, it slammed into a wall. [00:13:51] And I just remember sitting
there alone in a deep sadness, [00:13:56] sort of full of regret,
I think, almost anger, [00:14:03] but also, like, sadness
because you think about, [00:14:06] well, these robots, especially
for autonomous vehicles, [00:14:10] like, you should be taking
safety very seriously [00:14:12] even in these kinds of things,
but just no good feelings. [00:14:17] It made me more afraid
probably to do these kind [00:14:19] of experiments in the future. [00:14:20] Perhaps the right way to
have seen that is positively. [00:14:24] Like, it's too- [00:14:25] - It depends if you
could have built that car [00:14:28] or just gotten another one, right? [00:14:29] That would've been the approach. [00:14:32] I remember when I got to grad school, [00:14:38] you know, I got some training
about operating a lathe [00:14:42] and a mill up in the machine shop, [00:14:45] and I could start to make my own parts. [00:14:47] And I remember breaking some
piece of equipment in the lab [00:14:52] and then realizing 'cause
maybe this was a unique part, [00:14:55] and I couldn't go buy it, and I realized, [00:14:57] "Oh, I can just go make it." [00:15:00] That was an enabling feeling. [00:15:02] - [Lex] Yeah. [00:15:03] - Then, you're not afraid. [00:15:04] It might take time. [00:15:05] It might take more work than you thought [00:15:07] it was gonna be required
to get this thing done, [00:15:10] but you can just go make it. [00:15:12] And that's freeing in a
way that nothing else is. [00:15:16] - You mentioned the feedback
control, the dynamics, [00:15:20] sorry for the romantic question, [00:15:22] but in the early days and
even now, is the dynamics, [00:15:26] probably more appropriate
for the early days, [00:15:28] is it more art or science? [00:15:33] - There's a lot of science
around it, and trying to develop, [00:15:37] you know, scientific principles
that let you extrapolate [00:15:41] from, like, one legged machine to another, [00:15:44] you know, develop a core set of principles [00:15:48] like a spring-mass bouncing
system and then figure out how [00:15:53] to apply that from a one-legged machine [00:15:54] to a two- or a four-legged machine. [00:15:56] Those principles are really important [00:15:59] and were definitely a
core part of our work. [00:16:04] There's also, you know, when we started [00:16:08] to pursue humanoid robots,
there was so much complexity [00:16:12] in that machine that, you
know, one of the benefits [00:16:17] of the humanoid form is
you have some intuition [00:16:19] about how it should
look while it's moving. [00:16:22] And that's a little
bit of an art, I think, [00:16:26] or maybe it's just
tapping into a knowledge [00:16:28] that you have deep in
your body and then trying [00:16:31] to express that in the machine,
but that's an intuition [00:16:34] that's a little bit more on the art side. [00:16:37] Maybe it predates your knowledge. [00:16:39] Before you have the knowledge
of how to control it, [00:16:41] you try to work through
the art channel. (laughs) [00:16:43] - [Lex] Yeah.
- And humanoids sort [00:16:44] of make that available to you. [00:16:45] If it had been a different shape, [00:16:47] maybe you wouldn't have had
the same intuition about it. [00:16:50] - Yeah, so your knowledge about moving [00:16:53] through the world is not
made explicit to you. [00:16:58] That's why it's art. [00:17:00] - Yeah, it might be hard to
actually articulate exactly. [00:17:02] (laughing) You know?
- Yeah. [00:17:04] - And being a competitive athlete, [00:17:07] there's something about seeing a movement. [00:17:10] You know, a coach, one
of the greatest strengths [00:17:13] a coach has is being
able to see, you know, [00:17:16] some little change in
what the athlete is doing [00:17:18] and then being able to
articulate that to the athlete, [00:17:20] you know, and then maybe
even trying to say, [00:17:22] "And you should try to feel this." [00:17:25] So, there's something just in seeing, [00:17:28] and again, you know, sometimes
it's hard to articulate [00:17:31] what it is you're seeing, but
just perceiving the motion [00:17:35] at a rate that is, again,
sometimes hard to put into words. [00:17:41] - Yeah, I wonder how it is
possible to achieve sort [00:17:47] of truly elegant movement. [00:17:49] You have a movie like "Ex Machina." [00:17:51] I'm not sure if you've seen it, [00:17:53] but the main actress in
that who plays the AI robot [00:17:57] I think is a ballerina. [00:17:58] I mean, just the natural elegance [00:18:02] and the, I don't know,
eloquence of movement, (laughs) [00:18:08] it looks efficient and easy,
and just it looks right. [00:18:13] It looks beautiful.
- It looks right is [00:18:14] sort of the key, yeah? [00:18:15] - And then, you look at,
especially early robots, [00:18:18] I mean, they're so cautious
in the way they move [00:18:23] that it's not the
caution that looks wrong. [00:18:27] It's something about the
movement that looks wrong [00:18:30] that feels like it's very
inefficient, unnecessarily so. [00:18:34] And it's hard to put
that into words exactly. [00:18:38] - We think that, and part of the reason [00:18:40] why people are attracted
to the machines we build is [00:18:44] because the inherent dynamics [00:18:45] of movement are closer to right [00:18:49] because we try to use,
you know, walking gaits, [00:18:53] or we build a machine around this gait [00:18:55] where you're trying to work
with the dynamics of the machine [00:18:58] instead of to stop them. [00:19:01] You know, some of the early
walking machines, you know, [00:19:03] you're essentially,
you're really trying hard [00:19:06] to not let them fall over, [00:19:08] and so you're always stopping
the tipping motion, you know. [00:19:12] And sort of the insight
of dynamic stability [00:19:16] in a legged machine is to go
with it, you know, (laughs) [00:19:19] let the tipping happen. [00:19:21] You know, let yourself fall, [00:19:22] but then catch yourself
with that next foot. [00:19:24] And there's something
about getting those physics [00:19:27] to be expressed in the
machine that people interpret [00:19:30] as lifelike, or elegant, [00:19:36] or just natural looking. [00:19:38] And so, I think if you
get the physics right, [00:19:41] it also ends up being
more efficient, likely. [00:19:44] There's a benefit that it probably ends [00:19:45] up being more stable in the long run. [00:19:49] You know, it could walk
stably over a wider range [00:19:53] of conditions, and it's more beautiful [00:19:57] and attractive at the same time. [00:19:58] - So, how hard is it to get
the humanoid robot Atlas [00:20:03] to do some of the things that
it's recently been doing? [00:20:06] Let's forget the flips and all of that. [00:20:08] Let's just look at the running. [00:20:10] Maybe you can correct me, [00:20:11] but there's something about running. [00:20:12] I mean, that's not careful at all. [00:20:14] That's you're falling forward. [00:20:16] You're jumping forward and are falling. [00:20:18] So, (laughing) how hard
is it to get that right? [00:20:20] - Our first humanoid, we needed to deliver [00:20:23] natural-looking walking, you know. [00:20:25] We took a contract from the army. [00:20:27] They wanted a robot that
could walk naturally. [00:20:31] They wanted to put a suit on the robot [00:20:33] and be able to test it
in a gas environment. [00:20:36] And so, they wanted the
motion to be natural. [00:20:41] And so, our goal was a
natural-looking gait. [00:20:44] It was surprisingly hard
to get that to work. [00:20:48] But we did build an early machine. [00:20:51] We called it PETMAN prototype. [00:20:53] It was the prototype
before the PETMAN robot, [00:20:57] and it had a really nice-looking gait [00:21:01] where, you know, it
would stick the leg out. [00:21:03] It would do heel strike first
before it rolled onto the toe, [00:21:06] so you didn't land with a flat foot. [00:21:08] You extended your leg a little bit, [00:21:11] but even then it was hard
to get the robot to walk [00:21:14] where, when you were walking,
that it fully extended its leg [00:21:17] and essentially landed on an extended leg. [00:21:20] And if you watch closely how you walk, [00:21:22] you probably land on an extended leg, [00:21:24] but then you immediately flex your knee [00:21:25] as you start to make that contact, [00:21:28] and getting that all to work
well took such a long time. [00:21:32] In fact, I probably didn't really see [00:21:36] the nice, natural walking that I expected [00:21:38] out of our humanoids
until maybe last year. [00:21:42] And the team was developing
on our newer generation [00:21:45] of Atlas, you know, some new techniques [00:21:49] for developing a
walking-control algorithm. [00:21:52] And they got that
natural-looking motion as sort [00:21:55] of a byproduct of just a different process [00:21:58] they were applying to
developing the control. [00:22:01] So, that probably took 15
years, 10 to 15 years to sort [00:22:05] of get that from, you know, [00:22:08] the PETMAN prototype was probably
in 2008, and what was it, [00:22:11] 2022, (laughs) last year [00:22:13] that I think I saw good walking on Atlas. [00:22:15] - If you could just, like, linger on it, [00:22:17] what are some challenges
of getting good walking? [00:22:19] So, is this partially, [00:22:24] like, a hardware, like, actuator problem? [00:22:27] Is it the control? [00:22:29] Is it the artistic
element of just observing [00:22:31] the whole system operating in
different conditions together? [00:22:34] I mean, is there some
kind of interesting quirks [00:22:38] or challenges you can speak
to, like the heel strike [00:22:40] or all this kind of stuff?
- Yeah, so one [00:22:41] of the things that makes,
like, this straight leg [00:22:44] a challenge is you're sort
of up against a singularity, [00:22:49] a mathematical singularity
where, you know, [00:22:52] when when your leg is fully extended, [00:22:53] it can't go further the
other direction, right? [00:22:57] You can only move in one
direction, and that makes all [00:22:59] of the calculations around
how to produce torques [00:23:03] at that joint or positions
makes it more complicated. [00:23:07] And so, (laughs) having
all of the mathematics [00:23:09] so it can deal with these
singular configurations is one [00:23:15] of many (laughs) challenges that we face. [00:23:19] And I'd say, you know, in
those earlier days, again, [00:23:23] we were working with these
really simplified models. [00:23:27] So, we're trying to boil all the physics [00:23:29] of the complex human body
into a simpler subsystem [00:23:34] that we can more easily
describe in mathematics. [00:23:36] And sometimes those simpler
subsystems don't have all [00:23:39] of that complexity of the
straight leg built into them. [00:23:43] And so, what's happened
more recently is we're able [00:23:47] to apply techniques that
let us take the full physics [00:23:50] of the robot into account [00:23:53] and deal with some of
those strange situations [00:23:58] like the straight leg. [00:23:59] - So, is there a fundamental
challenge here that it's, [00:24:02] maybe you can correct me,
but is it underactuated? [00:24:05] Are you falling? [00:24:06] - Underactuated is the right word, right? [00:24:09] You can't push the robot in
any direction you want to. [00:24:12] - Yeah.
- Right? [00:24:12] And so, that is one of the hard problems [00:24:15] of legged locomotion. [00:24:16] - And you have to do that
for natural movement? [00:24:20] - It's not necessarily
required for natural movement. [00:24:22] It's just required, you know,
we don't have, you know, [00:24:26] a gravity force that you can
hook yourself onto to apply [00:24:30] an external force in
the direction you want [00:24:32] at all times, right? [00:24:33] The only external forces
are being mediated [00:24:36] through your feet, and how
they get mediated depend [00:24:38] on how you place your feet,
and you know, you can't just, [00:24:43] you know, God's hand
can't reach down and push [00:24:46] in any direction you want,
(laughs) you know, so. [00:24:50] - Is there some extra
challenge to the fact [00:24:52] that Atlas is such a big robot? [00:24:54] - There is. [00:24:55] The humanoid form is
attractive in many ways, [00:24:59] but it's also a challenge in many ways. [00:25:03] You have this big upper
body that has a lot [00:25:06] of mass and inertia, and
throwing that inertia [00:25:09] around increases the complexity
of maintaining balance. [00:25:14] And as soon as you pick up
something heavy in your arms, [00:25:16] you've made that problem even harder. [00:25:19] And so, in the early work in the Leg Lab [00:25:23] and in the early days at
the company, you know, [00:25:25] we were pursuing these quadruped robots, [00:25:28] which had a kind of
built-in simplification. [00:25:31] You had this big rigid body
and then really light legs. [00:25:34] So, when you swing the legs, [00:25:36] the leg motion didn't impact
the body motion very much. [00:25:41] All the mass and inertia was in the body, [00:25:43] but when you have the
humanoid, that doesn't work. [00:25:45] You have big heavy legs. [00:25:47] You swing the legs. [00:25:48] It affects everything else. [00:25:49] (Lex laughs) [00:25:50] And so, dealing with all of
that interaction does make [00:25:54] the humanoid a much more
complicated platform. [00:25:58] - And I also saw that at least
recently you've been doing [00:26:01] more explicit modeling
of the stuff you pick up. [00:26:04] - [Robert] Yeah, yeah. [00:26:05] - Which is (laughs) really interesting. [00:26:09] So, you have to, what, model the shape, [00:26:13] the weight distribution. [00:26:16] I don't know, like, you
have to, like, include that [00:26:19] as part of the modeling,
as part of the planning [00:26:21] 'cause okay, so for people
who don't know, so Atlas, [00:26:25] at least in, like, a recent
video, like, throws a heavy bag, [00:26:29] throws a (laughing) bunch of- [00:26:30] - [Robert] Yeah. [00:26:31] - stuff. [00:26:32] So, what's involved in picking
up a thing, a heavy thing? [00:26:37] And when that thing is a bunch [00:26:38] of different non-standard things, [00:26:40] I think it also picked up like a barbell [00:26:43] and to be able to throw in some cases, [00:26:46] what are some interesting
challenges there? [00:26:48] - So, we were definitely
trying to show that the robot [00:26:51] and the techniques we're
applying to Atlas let us deal [00:26:56] with heavy things in the world. [00:26:58] Because if the robot's gonna be useful, [00:26:59] it's actually gotta move stuff around. [00:27:02] And that needs to be significant stuff [00:27:04] that's an appreciable portion [00:27:06] of the body weight of the robot. [00:27:08] And we also think this differentiates us [00:27:11] from the other humanoid robot activities [00:27:13] that you're seeing out there. [00:27:14] Mostly, they're not picking stuff up yet, [00:27:16] not heavy stuff anyway. [00:27:19] But just like you or me, you know, [00:27:21] you need to anticipate that moment. [00:27:22] You know, you're reaching
out to pick something up, [00:27:24] and as soon as you pick it up, [00:27:25] your center of mass is gonna shift. [00:27:27] And if you're gonna, you
know, turn in a circle, [00:27:31] you have to take that
inertia into account. [00:27:33] And if you're gonna
throw a thing, you know, [00:27:36] all of that has to be sort of included [00:27:38] in the model of what you're trying to do. [00:27:41] So, the robot needs to have
some idea or expectation [00:27:44] of what that weight is and
sort of predict, you know, [00:27:48] think a couple of seconds ahead, [00:27:49] "How do I manage now my body
plus this big heavy thing [00:27:54] together (laughs) and still
maintain balance, right?" [00:27:58] And so, that's a big change for us, [00:28:03] and I think the tools we've
built are really allowing [00:28:06] that to happen quickly now. [00:28:08] Some of those motions that you
saw in that most recent video [00:28:12] we were able to create
in a matter of days. [00:28:15] It used to be that it took
six months to do anything new, [00:28:17] you know, on the robot, and
now we're starting to develop [00:28:20] the tools that let us do
that in a matter of days. [00:28:22] And so, we think that's really exciting. [00:28:24] That means that the ability
to create new behaviors [00:28:27] for the robot is gonna
be a quicker process. [00:28:31] - So, being able to
explicitly model new things [00:28:34] that it might need to pick
up, new types of things? [00:28:37] - And you know, to some degree, [00:28:39] you don't wanna have to
pay too much attention [00:28:41] to each specific thing, right? [00:28:45] There's sort of a generalization here. [00:28:49] Obviously, when you grab a thing, [00:28:51] you have to conform your
hand, your end effector [00:28:53] to the surface of that shape,
but once it's in your hands, [00:28:57] it's probably just the mass
and inertia that matter, [00:29:00] and the shape may not be as important. [00:29:03] - [Lex] Yeah. [00:29:03] - And so, you know, in some
ways you wanna pay attention [00:29:07] to that detailed shape, and in others, [00:29:09] you wanna generalize it and say, [00:29:11] "Well, all I really care about is [00:29:13] the center of mass of this thing, [00:29:14] especially if I'm gonna throw
it up on that scaffolding." [00:29:17] - And it's easier if the body is rigid. [00:29:19] What if there's some, doesn't it throw, [00:29:21] like, a sandbag type thing?