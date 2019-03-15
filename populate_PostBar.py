import os
from datetime import datetime
from typing import List

from autofixture import AutoFixture

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Post_Bar.settings')
import django

django.setup()
from PostBar.models import Category, Question, Answer, UserProfile
from django.contrib.auth.models import User


def populate():
    default_question_image_url = "question_images/default.png"
    default_answer_image_url = "answer_images/default.png"
    user1, profile1 = create_or_get_user_profile("john", 'jlennon@beatles.com', "passowrd", "nyu", "a@b.com", "daycare")
    user2, profile2 = create_or_get_user_profile("mary", 'mary@beatles.com', "passowrd", "nyu", "a@b.com", "daycare")
    user3, profile3 = create_or_get_user_profile("tom", 'Tom@beatles.com', "passowrd", "what", "a@b.com", "daycare")
    user4, profile4 = create_or_get_user_profile("jack", 'jack@beatles.com', "passowrd", "nyu", "a@b.com", "daycare")
    user5, profile5 = create_or_get_user_profile("mr square", 'square@beatles.com', "passowrd", "nyu", "a@b.com",
                                                 "daycare")
    user6, profile6 = create_or_get_user_profile("crazyworld", 'jack@beatles.com', "passowrd", "nyu", "a@b.com",
                                                 "daycare")
    profile1.add_following(user2.id)
    profile2.add_following(user1.id)
    profile3.add_following(user5.id)
    profile4.add_following(user3.id)
    profile5.add_following(user4.id)
    profile6.add_following(user5.id)

    math_answers = [
        {
            "answer_content": "I can swim and you can not",
            "answer_username": user1.username,
            "user": user1,
            "rank_counts": 12,
            "rank_points": 115},
        {
            "answer_content": "well that it to combine something togather",
            "answer_username": user1.username,
            "user": user1,
            "rank_counts": 12,
            "rank_points": 13
        },
    ]

    math_answers1 = [
        {
            "answer_content": "i think that is just representing sum of how many same number adding together",
            "answer_username": user3.username,
            "user": user3,
            "rank_counts": 13,
            "rank_points": 15},
        {
            "answer_content": "Try to understand it like group of number adding together,for example,2*3 = 3 + 3",
            "answer_username": user1.username,
            "user": user1,
            "rank_counts": 120,
            "rank_points": 1138},
    ]

    math_answers2 = [
        {
            "answer_content": "i think that is just representing sum of how many same number adding together",
            "answer_username": user2.username,
            "user": user2,
            "rank_counts": 13,
            "rank_points": 15},
        {
            "answer_content": "Try to understand it like group of number adding together,for example,2*3 = 3 + 3",
            "answer_username": user1.username,
            "user": user1,
            "rank_counts": 120,
            "rank_points": 1138},
    ]

    math_answers3 = [
        {
            "answer_content": "i think that you could take look of the vido that has been uploaded",
            "answer_username": user2.username,
            "user": user2,
            "rank_counts": 134,
            "rank_points": 151},
        {
            "answer_content": "the taylor series is ...............",
            "answer_username": user3.username,
            "user": user3,
            "rank_counts": 121,
            "rank_points": 118},
    ]

    computing_science_answers1 = [
        {
            "answer_content": "In bubble sort in ith iteration you have n-i-1 inner iterations (n^2)/2 total, "
                              "but in insertion sort you have maximum i iterations on i'th step, but i/2 on average, "
                              "as you can stop inner loop earlier, after you found correct position for the current "
                              "element. So you have (sum from 0 to n) / 2 which is (n^2) / 4 total;",
            "answer_username": user3.username,
            "user": user3,
            "rank_counts": 2201,
            "rank_points": 230,
        },
        {
            "answer_content": "In insertion sort elements are bubbled into the sorted section, "
                              "while in bubble sort the maximums are bubbled out of the unsorted section.",
            "answer_username": user3.username,
            "user": user3,
            "rank_counts": 12,
            "rank_points": 130},
    ]

    computing_science_answers = [
        {
            "answer_content": "just to take the exercise at page 121",
            "answer_username": user5.username,
            "user": user5,
            "rank_counts": 221,
            "rank_points": 230,
            "image_url": "answer_images/25788.jpg"
        },
        {
            "answer_content": "read them multiple times",
            "answer_username": user4.username,
            "user": user4,
            "rank_counts": 12,
            "rank_points": 136},
    ]

    computing_science_answers2 = [
        {
            "answer_content": "When we're inserting an element, we alternate comparisons and swaps until either (1) "
                              "the element compares not less than the element to its right (2) we hit the beginning of"
                              " the array. In case (1), there is one comparison not paired with a swap. In case (2), "
                              "every comparison is paired with a swap. The upward adjustment for number of comparisons "
                              "can be computed by counting the number of successive minima from left to right"
                              " (or however your insertion sort works), in time O(n).",
            "answer_username": user1.username,
            "user": user1,
            "rank_counts": 22,
            "rank_points": 230},
        {
            "answer_content": "As commented, to do it in less than O(n^2) is hard, maybe impossible "
                              "if you must pay the "
                              "price for sorting. If you already know the number of comparisons done at each external"
                              " iteration then it would be possible in O(n), but the price for sorting was "
                              "payed sometime before.",
            "answer_username": user4.username,
            "user": user4,
            "rank_counts": 12,
            "rank_points": 13},
    ]

    computing_science_answers3 = [
        {
            "answer_content": "just to take the exercise at page 121",
            "answer_username": user5.username,
            "user": user5,
            "rank_counts": 22,
            "rank_points": 230},
        {
            "answer_content": "When you deal with this fixed size take a look at Sorting Networks. "
                              "These algorithms have a fixed runtime and are independent to their input. "
                              "For your use-case you don't have such overhead that some sorting algorithms have.",
            "answer_username": user6.username,
            "user": user6,
            "rank_counts": 12,
            "rank_points": 13},
    ]

    other_answers = [
        {
            "answer_content": "Yes of course ",
            "answer_username": user1.username,
            "user": user1,
            "rank_counts": 12,
            "rank_points": 131},
        {
            "answer_content": "No doubt",
            "answer_username": user1.username, "rank_counts": 12,
            "user": user1,
            "rank_points": 131}

    ]

    other_answers1 = [
        {
            "answer_content": "I am a vigilant and proactive Security Officer working to ensure safe, secure, "
                              "and orderly environments. I’m also a lifelong learner, always seeking out the"
                              " latest security equipment and techniques to patrol buildings. Lastly, I am thorough, "
                              "documenting all incidents and actively making suggestions to"
                              " management about security improvements and changes.",
            "answer_username": user6.username,
            "user": user6,
            "rank_counts": 123,
            "rank_points": 131},
        {
            "answer_content": "I am highly organized. I always take notes, and I use a series of tools to "
                              "help myself stay on top of deadlines. I like to keep a clean workspace and "
                              "create a logical filing method so I’m always able to find what I need. "
                              "I find this increases efficiency and helps the rest of the team stay on track,"
                              " too. In my last role, I created a new filing process that increased departmental "
                              "efficiency 25%.",
            "answer_username": user3.username, "rank_counts": 127,
            "user": user3,
            "rank_points": 131}

    ]

    other_answers2 = [
        {
            "answer_content": "Currently, I serve as the assistant to three of the company’s five executive team"
                              " members, including the CEO. During my time at the organization, "
                              "I have been recognized for my time management skills, writing abilities"
                              " and commitment to excellence.From my 12 years of "
                              "experience as an executive assistant, I’ve developed the ability"
                              " to anticipate roadblocks and create effective alternative plans. "
                              "My greatest value to any executive is my ability to work independently,"
                              " freeing up their time to focus on the needs of the business."
                              "It’s clear that you’re looking for someone who understands "
                              "the nuances of managing a CEO’s busy day and can proactively tackle issues."
                              " As someone with a sharp eye for detail and a drive to organize, "
                              "I thrive on making sure every day has a clear plan and every "
                              "plan is clearly communicated.",
            "answer_username": user1.username,
            "user": user1,
            "rank_counts": 12,
            "rank_points": 131},
        {
            "answer_content": "Mention past experiences and proven successes as they relate to the position."
                              " Begin by rereading the job description. Take note of the required skills that you have,"
                              " and identify recent stories that demonstrate them "
                              "(review the STAR method to practice telling great stories in your interviews). "
                              "Ideally, you should draw primarily from recent professional experience; however, "
                              "volunteer work can also support your narrative "
                              "while demonstrating a commitment to your community.Consider how your current "
                              "job relates to the job you’re applying for. Is it a more senior role? If so,"
                              " explain how you are taking on more responsibilities in your current position. "
                              "If you are making a lateral transition to a role with different skills, "
                              "describe how your current skills translate into the new position."
                              "Focus on strengths and abilities that you can support with examples. "
                              "When you start building the script of each example, focus on details "
                              "and outcomes that you can quantify if possible. For example, "
                              "stating that you “improved customer service” is less impactful "
                              "than “increased customer service response rates each quarter by 10–15%.”"
                              " If you don’t have the exact information, estimate a realistic value"
                              ".Highlight your personality to break the ice. Because the “Tell me about yourself” "
                              "interview question is about getting to know you, it’s a good idea to share your "
                              "personality with your interviewer—but not personal details. "
                              "You may want to briefly mention hobbies that demonstrate intellectual development"
                              " and/or community engagement (e.g., reading, music, sports league, volunteering) "
                              "or those that showcase personal discipline and achievement "
                              "(e.g., learning a new skill, training for a half marathon). "
                              "Discussing personal interests "
                              "is a good way to wrap up your response while maintaining a professional tone.",
            "answer_username": user4.username,
            "rank_counts": 1234,
            "user": user4,
            "rank_points": 131}

    ]

    other_answers3 = [
        {
            "answer_content": "What makes me unique is my experience of four years in retail."
                              " Because I’ve had first-hand experience fielding shoppers’ questions, "
                              "feedback and complaints, I know what customers want. "
                              "I know what it takes to create a positive consumer experience through marketing.",
            "answer_username": user1.username,
            "user": user1,
            "rank_counts": 116,
            "rank_points": 131},
        {
            "answer_content": "Instead of trying to identify a feature that distinguishes you from all "
                              "other applicants, focus instead on why hiring you would "
                              "benefit the employer. Since you don’t know the other applicants,"
                              " it can be challenging to think about your answer in relation to them."
                              " Addressing why your background makes you a good fit will let employers"
                              " know why your traits and qualifications make you well prepared.Here are "
                              "four things you can do to help you identify your most relevant, unique traits:"
                              "Consider what the employer may find valuable Employers want candidates who will"
                              " bring a perspective, skill set or ability that will help them achieve business goals. "
                              "Take time to carefully review the job description and look for information "
                              "about specific objectives the employer is hoping the new employee will meet,"
                              " then identify the strengths you possess that align with these needs.For example, "
                              "if you’re applying for a team management position and the job description highlights "
                              "the company’s drive to facilitate cross-department communication, "
                              "you might share your ability to bring people together around a"
                              " common goal and create drive in a group setting.Look to your background"
                              " and previous experiences.Think back on times you were successful "
                              "in previous positions or times you were praised or rewarded by your "
                              "employer. What did you do to earn recognition? What traits,"
                              " skills or abilities helped you achieve success? Whatever"
                              " you accomplished is likely something other employers would also"
                              " appreciate in a new employee.For example, a particularly gifted "
                              "sales professional may have experience handling unhappy clients "
                              "or bringing back lost accounts. In this case, their unique skill "
                              "may be their ability to perceive when someone is unhappy and "
                              "quickly mobilize a strategy to diffuse and address their concerns."
                              "Acknowledge your most popular personality traits.Consider strengths "
                              "highlighted by previous employees and traits your friends and family "
                              "have celebrated. Then, look for ways you could apply these aspects of "
                              "your personality to excel in the job.For example, let’s say other people"
                              " have recognized you’re patient and dedicated. In this case, you could"
                              " share how your patience and persistence has allowed you to remain calm "
                              "and collected in high-stress scenarios or your determination to meet goals "
                              "despite outside pressures or setbacks.Remember: You don’t have to be a one-of-a-kind."
                              "Don’t let the word “unique” confuse or intimidate you. While employers are looking for "
                              "interesting skills, they don’t expect you to share something that’s unlike any answer "
                              "they’ve ever heard—especially if it’s not relevant to the job.For example, "
                              "if you’re applying for a customer service position, the employer probably "
                              "isn’t interested in hearing about your unique trapeze skills. Alternatively, "
                              "fluency in multiple languages might not be especially uncommon but this valuable "
                              "skill may be enough to set a customer service candidate apart from other applicants."
                              "Pro-tip: If you’ve received peer or manager feedback that highlights some of"
                              " your strengths, you could include this in your answer. This can provide "
                              "further evidence for the traits you claim to have. For example, you might "
                              "begin your response by saying: “In my peer feedback, I’ve been regularly "
                              "recognized for my ability to collaborate…” You can then go into more detail"
                              ".When answering any interview question, use specific details or real-life scenarios "
                              "whenever possible. The better you demonstrate your abilities through examples, "
                              "the more memorable and reliable your answer.Related: Top 16 Interview Questions "
                              "and AnswersHow to answer “Tell us what makes you unique” (with examples)Here are a "
                              "few sample responses to help you determine how to answer “What makes you unique?”:"
                              "“My natural ability to organize effectively makes me unique. In my previous role as "
                              "an administrative assistant, I came up with a plan to reorganize the office supply "
                              "closet by category. Because items were easier to find, we placed fewer orders and"
                              " saved 30% on office supplies year-over-year.”“What makes me unique is my ability"
                              " to easily empathize with and relate to people. This skill helped me in my previous "
                              "role as an account executive in charge of prospecting new accounts. Because I was able "
                              "to quickly identify and understand their pain points and challenges, "
                              "I was able to establish trust and build relationships—both of which drove me"
                              " to consistently exceed my quota.”“What makes me unique is my experience of four"
                              " years in retail. Because I’ve had first-hand experience fielding shoppers’ questions, "
                              "feedback and complaints, I know what customers want. I know what it takes to create a"
                              " positive consumer experience through marketing.”Everyone has something special that"
                              " makes them an ideal candidate for a job. By identifying your unique strengths and "
                              "composing your talking points before your interview, you can be prepared to communicate "
                              "why you’re a great fit for the job.",
            "answer_username": user2.username, "rank_counts": 12632,
            "user": user2,
            "rank_points": 131}

    ]

    history_answers1 = [
        {
            "answer_content": "England ",
            "answer_username": user3.username,
            "user": user3,
            "rank_counts": 121,
            "rank_points": 131},
        {
            "answer_content": "England and scotland",
            "answer_username": user4.username, "rank_counts": 124,
            "user": user4,
            "rank_points": 131}

    ]

    history_answers = [
        {
            "answer_content": "Pompey",
            "answer_username": user2.username,
            "user": user2,
            "rank_counts": 126,
            "rank_points": 131,
        },
        {
            "answer_content": "pompey, of course",
            "answer_username": user1.username, "rank_counts": 123,
            "user": user1,
            "rank_points": 131}

    ]

    history_answers2 = [
        {
            "answer_content": "Ivan IV (the Terrible)",
            "answer_username": user1.username,
            "user": user1,
            "rank_counts": 121,
            "rank_points": 131},
        {
            "answer_content": "interesting...",
            "answer_username": user5.username, "rank_counts": 1,
            "user": user5,
            "rank_points": 1}

    ]

    history_answers3 = [
        {
            "answer_content": " Blue Shift",
            "answer_username": user6.username,
            "user": user6,
            "rank_counts": 12,
            "rank_points": 131},
        {
            "answer_content": "donno",
            "answer_username": user1.username, "rank_counts": 1,
            "user": user1,
            "rank_points": 1}

    ]

    physics_answers = [
        {
            "answer_content": "A flight simulator",
            "answer_username": user6.username,
            "user": user6,
            "rank_counts": 121,
            "rank_points": 131},
        {
            "answer_content": "A flight simulator",
            "answer_username": user5.username, "rank_counts": 1,
            "user": user5,
            "rank_points": 1}

    ]

    physics_answers1 = [
        {
            "answer_content": "Amperes",
            "answer_username": user5.username,
            "user": user5,
            "rank_counts": 122,
            "rank_points": 131},
        {
            "answer_content": "Volt?",
            "answer_username": user4.username, "rank_counts": 0,
            "user": user4,
            "rank_points": 0}

    ]

    physics_answers2 = [
        {
            "answer_content": " Scotland",
            "answer_username": user3.username,
            "user": user3,
            "rank_counts": 12,
            "rank_points": 131},
        {
            "answer_content": "England?",
            "answer_username": user2.username, "rank_counts": 0,
            "user": user2,
            "rank_points": 0}

    ]

    physics_answers3 = [
        {
            "answer_content": "Big bang",
            "answer_username": user2.username,
            "user": user2,
            "rank_counts": 120,
            "rank_points": 131},
        {
            "answer_content": "Big bang",
            "answer_username": user1.username, "rank_counts": 100,
            "user": user1,
            "rank_points": 100}

    ]

    math_questions = [
        {
            "question_title": "What is the differentiation?",
            "question_content": "I heard a lot about differentiation during hight school,what is that exactly",
            "answer_username": user1.username,
            "user": user1,
            "id": 0,
            "views": 31,
            "likes": 12,
            "question_isComplete": True,
            "latest_question_published": "2009-11-13",
            "answers": math_answers
        },
        {
            "question_title": "What is the multiplication?",
            "question_content": "basically,can anybody explain t to me?",
            "user": user3,
            "views": 310,
            "likes": 121,
            "question_isComplete": True,
            "latest_question_published": "2003-10-13",
            "answers": math_answers1
        },
        {
            "question_title": "What is the assignment for math1R?",
            "question_content": "I totally missed the lecture,and i wasn't informed",
            "user": user3,
            "id": 2,
            "views": 21,
            "likes": 10,
            "question_isComplete": True,
            "latest_question_published": "2009-11-24",
            "answers": math_answers2
        },
        {
            "question_title": "could any body give me any suggestion of how to do the question on the "
                              "text book at page 121?",
            "question_content": "that question is basically talking about taylor series",
            "user": user4,
            "id": 3,
            "views": 30,
            "likes": 11,
            "question_isComplete": True,
            "latest_question_published": "2002-12-13",
            "answers": math_answers3
        }
    ]

    computing_science_questions = [
        {
            "question_title": "How am i supposed to learn Cs?",
            "question_content": "cause it is so difficult for me!",
            "user": user1,
            "views": 34,
            "likes": 12,
            "question_isComplete": True,
            "latest_question_published": "2009-11-13",
            "answers": computing_science_answers,
            "image_url": "question_images/cs.jpg"
        },
        {
            "question_title": "Insertion sort vs Bubble Sort Algorithms",
            "question_content": "I'm trying to understand a few sorting algorithms, but I'm struggling to see the "
                                "difference in the bubble sort and insertion sort algorithm.",
            "user": user2,
            "views": 349,
            "likes": 122,
            "question_isComplete": True,
            "latest_question_published": "2015-9-13",
            "answers": computing_science_answers1
        },
        {
            "question_title": "Insertion Sort comparison?",
            "question_content": "How to count number of comparisons in insertion sort in less than O(n^2) ?",
            "user": user3,
            "views": 344,
            "likes": 121,
            "question_isComplete": True,
            "latest_question_published": "2013-9-12",
            "answers": computing_science_answers2
        },
        {
            "question_title": "Fastest way to sort 10 numbers? (numbers are 32 bit)",
            "question_content": "I'm solving a problem and it involves sorting 10 numbers (int32) very quickly."
                                " My application needs to sort 10 numbers millions of times as fast as possible."
                                " I'm sampling a data set of billions of elements and every time "
                                "I need to pick 10 numbers out of it (simplified) and sort them"
                                " (and make conclusions from the sorted 10 element list).",
            "user": user4,
            "views": 345,
            "likes": 126,
            "question_isComplete": True,
            "latest_question_published": "2002-11-23",
            "answers": computing_science_answers3
        }
    ]

    other_questions = [
        {"question_title": "Do we have to attend any of the lectures?",
         "question_content": "i know is not correct to skip any lectures,however i think some of them is not that kind "
                             "of important",
         "user": user1,
         "views": 31,
         "likes": 12,
         "question_isComplete": True,
         "latest_question_published": "2009-11-13",
         "answers": other_answers
         },
        {"question_title": "How would you describe yourself",
         "question_content": "When an interviewer asks you to talk about yourself, "
                             "they’re looking for information about how your qualities "
                             "and characteristics align with the skills they believe are required to "
                             "succeed in the role. If possible, include quantifiable results to "
                             "demonstrate how you use your best attributes to drive success.",
         "user": user2,
         "views": 31,
         "likes": 12,
         "question_isComplete": True,
         "latest_question_published": "2017-11-13",
         "answers": other_answers1
         },
        {"question_title": "can you talk about yourself?",
         "question_content": "Your interviewers will likely start out with a question about yourself and "
                             "your background to get to know you. Start out by giving them an overview about "
                             "your current position or activities, then provide the most important and relevant"
                             " highlights from your background that make you most qualified for the role. "
                             "If you’d like, it is generally acceptable to include some light personal details "
                             "about things like your pets, hobbies or family. Doing so can help you be more "
                             "memorable and personable to the interviewer.",
         "user": user3,
         "views": 31,
         "likes": 12,
         "question_isComplete": True,
         "latest_question_published": "2009-11-13",
         "answers": other_answers2
         },
        {"question_title": "What makes you unique",
         "question_content": "Employers often ask this question to identify why you might be more qualified "
                             "than other candidates they’re interviewing. To answer, focus on why hiring you would"
                             " benefit the employer. Since you don’t know the other applicants, it can be challenging "
                             "to think about your answer in relation to them. Addressing why your "
                             "background makes you a good fit will let employers know why your traits "
                             "and qualifications make you well prepared.",
         "user": user4,
         "views": 31,
         "likes": 12,
         "question_isComplete": True,
         "latest_question_published": "2018-11-13",
         "answers": other_answers3
         }
    ]

    history_questions = [
        {
            "question_title": "like what content said",
            "question_content": " The First Triumvirate was established in 60 B.C. by Julius Caesar, Marcus "
                                "Licinius Crassus, and this Roman general and consul. He was one of Caesar's many "
                                "enemies and his son-in-law,he became a ruler of Rome. Who was he",
            "user": user1,
            "views": 304,
            "likes": 112,
            "question_isComplete": True,
            "latest_question_published": "2009-11-13",
            "answers": history_answers,
        },
        {
            "question_title": "please look the question",
            "question_content": "The 1513 Battle of Flodden "
                                "Field was the largest battle (in terms of numbers) ever "
                                "fought between which two countries",
            "user": user2,
            "views": 324,
            "likes": 120,
            "question_isComplete": True,
            "latest_question_published": "2003-11-13",
            "answers": history_answers1
        },
        {
            "question_title": "anybody know the time?",
            "question_content": "This Russian ruler was the first to be crowned Czar(Tsar) "
                                "when he defeated the boyars (influential families) in 1547. Who was he",
            "user": user3,
            "views": 335,
            "likes": 126,
            "question_isComplete": True,
            "latest_question_published": "2001-11-13",
            "answers": history_answers2
        },
        {
            "question_title": "please any body !!",
            "question_content": " ____ occurs when source of light approach an observer?",
            "user": user4,
            "views": 349,
            "likes": 127,
            "question_isComplete": True,
            "latest_question_published": "2003-11-13",
            "answers": history_answers3
        }
    ]

    physics_questions = [
        {
            "question_title": "about looking for answer",
            "question_content": "7. What state of the art computer technology "
                                "is used to train pilots when wanting to copy the experience of flying an aircraft?",
            "user": user1,
            "views": 341,
            "likes": 122,
            "question_isComplete": True,
            "latest_question_published": "2012-11-13",
            "answers": physics_answers
        },
        {
            "question_title": "please answer it",
            "question_content": " Electric current is typically measured in what units",
            "user": user2,
            "views": 194,
            "likes": 120,
            "question_isComplete": True,
            "latest_question_published": "2017-11-13",
            "answers": physics_answers1
        },
        {
            "question_title": "interesting question",
            "question_content": "Theoretical physicist James Maxwell was born in what country?",
            "user": user3,
            "views": 134,
            "likes": 182,
            "question_isComplete": True,
            "latest_question_published": "2014-11-13",
            "answers": physics_answers2
        },
        {
            "question_title": "Looking for answer",
            "question_content": "The most recognized model of how the universe begun is known as the?",
            "user": user4,
            "views": 300,
            "likes": 121,
            "question_isComplete": True,
            "latest_question_published": "2011-11-13",
            "answers": physics_answers3
        }
    ]

    Cats = {
        "Maths question": math_questions,
        "Computing Science": computing_science_questions,
        "Other Questions": other_questions,
        "History question": history_questions,
        "physics question": physics_questions,
    }

    for c, qs in Cats.items():
        cat = add_cat(c)
        for i, q in enumerate(qs):
            qa = add_question(cat, q["user"], q["question_title"], q["question_content"], q["views"], q["likes"],
                              q["latest_question_published"], q["question_isComplete"], q.get("image_url", default_question_image_url))
            q_answers = q["answers"]
            for ans in q_answers:
                add_answer(ans["user"], qa, content=ans["answer_content"],
                           rank_count=ans["rank_counts"],
                           rank_points=ans["rank_points"],
                           image_url=ans.get("image_url", default_answer_image_url))


def create_or_get_user_profile(username, email, password, location, webside, background):
    status = User.objects.filter(username=username, email=email).exists()
    if not status:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user_profile = UserProfile.objects.create(user=user, location=location, website=webside, background=background)
        user_profile.save()
    else:
        user = User.objects.filter(username=username, email=email).get()
        user_profile = user.userprofile
    return user, user_profile


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_question(category, user, title, content, views, likes, last_modified, completed, image_url=None):
    last_modified = datetime.strptime(last_modified, "%Y-%m-%d")
    q = Question.objects.create(user=user, category=category)
    q.picture = image_url
    q.title = title
    q.content = content
    q.views = views
    q.likes = likes
    q.last_modified = last_modified
    q.completed = completed
    q.save()
    return q


def add_answer(user: User, question: Question, content, rank_count=0, rank_points=0, image_url=None):
    a = Answer.objects.create(question=question, user=user, content=content)
    a.picture = image_url
    a.rank_count = rank_count
    a.rank_points = rank_points
    a.save()
    return a


def gen_save(class_type, n=10):
    fixture = AutoFixture(class_type)
    objs: List[Category] = fixture.create(n)
    for obj in objs:
        obj.save()


def save_all(objects: List[Category]):
    for o in objects:
        o.save()


if __name__ == '__main__':
    populate()
# gen_save(User)
# gen_save(Category)
# gen_save(Question, 50)
# gen_save(Answer, 1500)
# gen_save(UserProfile, 10)
