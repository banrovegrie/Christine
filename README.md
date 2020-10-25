# Christine

> "Our lives begin to end the day we become silent about things that matter." 
~ Martin Luther King Jr. 

**Christine** is a discord-bot that moderates sexual harassment along with toxicity and depressive behavior in the server. 

So go ahead! Use Christine to make your server a **safe place for all**!

## Table of Contents

- [About](#About)
    - [Our Idea](#Our-Idea)
    - [Technologies Involved](#Technologies-Involved)
    - [Automated Chat Moderator](#Automated-Chat-Moderator) 
- [Members](#Members)
- [Basic Working Version](#Basic-Working-Version)
    - [Features](#Features)
    - [Installation](#Installation)
    - [Implementation](#Implementation)
- [Further Ideas](#Further-Ideas)
- [License](LICENSE)

## About

### Introduction

Today, especially when the world lies in the grasps of the Corona-virus, a considerable amount of human interactions happen online. 

Chatting platforms such as Discord have become more important as the source of day to day interactions. It is of utmost  importance that we prevent spread of hatred, misogyny and negativity.

To combat this issue, we decided to develop Christine, named after the famous feminist writer Christine de Pizan, a discord bot that moderates **harassment** (esp. sexual harassment) and profanity as well as tries to keep a track and inform the administration regarding **patterns of depressive behavior** observed among the members of any certain server.

In short, this is our attempt to make a singular bot to stop **cyber-bullying, sexual-harassment** as well as provide a perfect tool for administrators to help out their friends and colleagues who might be **suffering with the painful gout of depression.**

<img src="https://cdn.discordapp.com/attachments/769945683511214080/769951413018689546/unknown.png">

### About Discord

Among the several instant messaging platforms available, **Discord** is one of the most popular ones. Because of its several innovative features like server-channel systems, awesome call quality, permission management and tools to integrate bots, Discord has become a major platform for people to collaborate, converse and share ideas.

**Why we chose discord?**

<img src="https://cdn.discordapp.com/attachments/769945683511214080/769945698455650314/unknown.png">

As is evident from the above **active user statistics** of discord, we can deduce that as the application is exponentially gaining users.

Many schools, workplaces and universities have started using discord as their main platform for both collaboration and social connection. However, there are absolutely no full-proof solutions to the problems we have mentioned in introduction.

### Our Idea

As has been mentioned earlier on this project, we aim to make a **Discord bot** that **moderates** chats on the discord server, and sends a report to human moderators, allowing them to curb negativity and toxic messages within the server.

This not only allows the moderators to identify offensive messages, but also provides the moderator with the corresponding **"trigger tag"** which allows the moderator to make a more informed decision.

The bot also supports multiple languages, using Google Translate API.

We intend to work on this bot (for a long term duration) and improve it further. We have several ideas that we are to implement next - which we could not yet, under the strict time constraints of the hackathon.

### Technologies Involved

- Python 3
- JavaScript
- Google Cloud for hosting the bot on a virtual machine
- `Discord.py` for functionality of discord bot

For a detailed description regarding the current implementation check [this](#Implementation).

### Automated Chat Moderator

Moderation of texts and posts online is very essential given the importance the internet and social media in our world. The task of moderation is done by social media companies such as Facebook, Twitter manually by moderators assisted by bots which help identify the potentially offensive text/post.

We are attempting a similar model for our discord bot where the bot will identify the concerning text or conversation, and inform the human moderators accordingly. 

Chats are inherently noisy, unstructured, informal and involves frequent shifts in topic. These issues make moderating a chat a very challenging task

Our current working version uses a **"bag of words"** approach to generate a score for the text message on various parameters such as toxicity, suicide or self-harm, profanity, racism, personal attack etc. These scores are used to determine whether the text must be reported or not, and classifies them into the corresponding "trigger-tag". For a detailed description on implementation of this model, look [here](#Implementation).

In [Further Ideas](#Further-Ideas), we also attempt at constructing a better algorithm for effective flagging of text messages, based on the research presently available on the topic.

## Members

The original team involved in the project comprises of: [Alapan Chaudhuri](https://github.com/banrovegrie), [Shivansh Subhramanium](https://github.com/AurumnPegasus), [Shreyas Pradhan](https://github.com/claretgrace0801), [Zeeshan Ahmed](https://github.com/Zshan0), [Abhishek Mittal](https://github.com/abhishekmittal15) and [Hrishi Narayanan](https://github.com/hr1sh1-coding), respectively.

# Basic Working Version

### Features

- Easy to use conversation moderator for messages on a discord server.
- Identifies the texts that are not appropriate in the server and reports to the moderator along with corresponding trigger tags.

## Installation

:warning: **This project uses Python 3**: Usage of Python 2 may have varying effect

- Create a virtual environment and install dependencies:

    ```python
    $ python3 -m venv .env
    $ . .env/bin/activate
    $ pip3 install -r requirements.txt
    ```

- Install the nltk corpus required:

    ```python
    $ python3 nltkmodules.py
    ```

- Export the required environment variables:

    ```bash
    $ export BOT_TOKEN="TOKEN_FOR_DISCORD_BOT"
    $ export BOT_PREFIX="PREFIX_FOR_BOT"
    ```

- Run the bot:

    ```python
    python3 main.py
    ```

## Implementation

### Application Backend

Most of this has been handled using python and json. We use the vibrant features of `Discord.py` to efficiently access and store messages for analysis.

Again, we use it to intimate server administrators (or owners) with triggers that have been generated by the analysis.

### Obtaining Big Data of 1.6 Million Tweets from Kaggle

Due to the similarity between tweets and messages on chat, We used Data from Kaggle which has labelled tweets of Depression scaling from 0 to 4.

### Model Training

The current model being used converts the sentences to vectors using Word2vectors model, it has 100 dimensions and uses continuous bag of words algorithm.

We are using a library(Word2vec) to convert our tweets to vectors. These vectors are of 100 dimensions, for each tweet we have a label. So by doing supervised training on models, we can calculate the depressive value for a message on a scale of 0 to 4 where 0 is highly depressed.

### Data Cleaning

- Since the tweets used had meta data of the websites, links and also a lot of spelling mistakes and slang. 
- We were able to fix most of it by doing lemmatization of the sentences using nltk library. 
- Lemmatization also skips the common words such as "the" "there", and converts words such as "swimming" to "swim" which makes the prediction much better.
- The library used for word2vec also cleans the data by combining similar words such as "Los Angeles" to "Los_Angeles" to increase the accuracy.

### Transformation

- We only had to transform the tweets once by fitting them into the Word2vec model created.
- That will load all the required vocabulary to the model and then later we fitted tweets on it which gave us the 100 dimensional vector. 
- The model used for transformation is stored in a binary file which can be loaded anytime.
- The model transforms each word into its respective vector using the model.
- We consider the weighted average of the words for calculating the word vector for the sentence, for the words which are not present in the vocabulary, that is the words which got filtered out in lemmatization, or had just too less number of occurrences.
- This gave us a vector of 100 dimensions for a respective tweet. We then had to do a supervised learning with 100 features and discrete labels. We trained multiple models to test but at the end we are just using one model.

### Models Used

- We started with basic linear regression which gave us an accuracy of 0.57. We then used KNN which also did not perform well.
- We finally ended up using Logistic regression on the features, we trained our model on 80% of the tweets and then later tested it on the remaining 20% of tweets which gave us an accuracy of 75.7%.

### Moderation Process

We need further work in this aspect. As of now we have implemented intimation procedures. More has been sketched out in [further ideas](#Further-Ideas).

## Further Ideas

### Regarding Moderation Algorithm

Now that we have explained our working version, we would like to elaborate upon how we plan to **better the moderation algorithm**.

The outcomes can be made much more accurate using a significantly larger datasets, compiled from different sources from across the internet. 

The current implementation uses "bag of words" for sentiment analysis. However, this approach is simplistic and naive, as it does not consider the context of the message properly which may cause misinterpretation of the message and incorrect tagging.

There are other more complex and algorithms that could do the task of scoring according to parameters much more accurate. These include mostly Recursive Deep Models, for example models based on a Sentiment Treebank.

A potential improvement would be developing a model that take a summary of the conversation or texts by the user of the flagged message, so that there is a better contextual basis to the flagging.

Having larger data from chat history and other sources like Facebook would also expand the vocabulary of the model and would be able to build stronger connections between the similar words.

Rather than using a vanilla machine learning model, we can fit a neural network and use deep learning to our advantage to get more accurate results. Using models such as LSTM would allow us to train on much larger text size rather than limiting ourselves to just the tweets.

### Statistics and Easy Access for Server Admins

After tackling the detection of harmful or abusive texts we now want to scale our current small model. Scaling implies larger servers both in terms of members and roles and permissions etc. But the no of admins have to be limited so that they can co-ordinate among themselves. This creates a requirement for a much more convenient way of server admins to be able to monitor the activity of the server. 

This model can be scaled by creating a web app which the server admins can access and get a clear understanding. This involves creating a visually appealing fronted which displays the statistics of the group.
1. The top 10 users who have sent the most number of abusive messages.
2. The no of abusive messages sent over the past 7 days. 
3. The number of people banned by the admins over a period of time
4. The proportion of the people indulging in abusive language. 
Now this can be made easily interpretative by the use of graphs. The graphs will be helpful in reducing the amount of time the admins would have to spend in the analytics of the group 

### On Recognizing Offensive Texts

Currently there is very little machinery on most online platforms to identify and prevent the spread of negativity. Social media companies largely rely on user reports to identify posts that violate the community norms and guidelines. 

Few companies use AI based models to help identify toxic messages on their platform. Other innovative methods include Instagram's Comment Warning and Feed Post Warning systems which uses AI specifically to get users to pause, reflect, and edit their words when they are about to post something potentially offensive or hurtful. However, task is largely complicated by the fact that messages and  may include images or videos, for which analysis is significantly difficult.

In conclusion, we feel that there is a need to develop better systems to prevent negativity in chatting platforms and social media in general.
