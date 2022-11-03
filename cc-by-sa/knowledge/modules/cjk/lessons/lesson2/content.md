# Japanese Typography Basics

A lot of scripts in the world use one script per language. But that’s not the case in Japan. When you write a sentence in Japanese, there will be three different scripts being used: _Hiragana_, _Katakana_, and _Kanji_, a Japanified version of Chinese characters. And if you’re trying to develop a Japanese typeface, you also need to include the Latin alphabet and figures in addition. Japanese is the only script among CJK that uses multiple scripts to form their language. How did it become such a melting pot of scripts? And what kind of unique aspects do they have?

[IMAGE: Comparison of Hiragana, Katakana, and Kanji]


## Development of Kana

Back in the days Japan was using Chinese characters to communicate in a written form, like other typical Asian countries did. In some cases they substituted the Chinese characters into the Japanese sound, and in others they used Kanji as ideogram, to communicate the context. Sometime around the 700s, Japan started to use their own Japanified version of Chinese characters, which is now called _Kanji_. And around the 800s, they invented _Hiragana_ and _Katakana_. They are called _Kana _altogether.

_Hiragana_ is a simplified version of _Kanji_—it uses simple curvy lines to write Kanji easier. It started as a cursive script of Kanji, and became the Hiragana letterform we use now. It was developed among women at first, because back in the days many women couldn’t have opportunities for education, and were not allowed in an official post which needed the use of Kanji-based writing. Hiragana was such a huge creative development and afterwards it became more and more popular regardless of gender and social status, and now a main script for Japanese.

[IMAGE: How Hiragana was developed from Kanji]

_Katakana_, on the other hand, was developed in a different way. It is an alternative form of _Hiragana_, and in modern times it’s often used to write foreign words. Katakana is also a simpler form of Kanji, but the difference from Hiragana is that while Hiragana simplifies the whole Kanji, Katakana takes only a part of Kanji and makes it into a new character. 

Katakana was created by monks; they needed an easier and less packed form of letters for their scriptures to write _Ruby_ next to Kanji. 

[IMAGE: How Katakana was developed from Kanji]


## Why still use Chinese characters “Kanji” in Japan?

In Korea, the usage of Chinese characters are fading away, and most of the news only use Hangeul, without any Chinese characters. Then, why does Japan still use Kanji? Many non-Japanese speaking readers will find this curious. 

The important thing we must not forget is that Hiragana and Katakana are phonograms, and Kanji is ideogram. Japanese words have many homonyms—words that sounds the same but mean completely different things—, so by using ideogram Kanji, it helps a lot in avoiding miscommunications. There’s another fact that Japanese doesn't have word spacing system, so without Kanji, it would be very hard to figure out where to cut the sentence. Also, by using Kanji in between, the sentence will be much shorter too. 


## Development of the letterform

Before the metal typesetting, Japanese was written in a script style due to the use of pointed brush. This meant that Hiragana was written in unbroken forms—in other words, every character was written connected, like Latin calligraphy. When they first started using the metal type in the 1500s, their Hiragana types had two or more characters altogether in one type like Latin ligatures, as you can see in the example below on the left. In the 1800s, after the seclusion policy in Japan was lifted, they imported Chinese metal types. Chinese metal types had one letter on each metal, and to adapted in this way, Japan started to develop “disconnected” Hiragana and Katakana that fit in the square embox. 

[IMAGE: Hiragana development of unbroken to disconnected]

And there’s more—an _alternative Kanji_. Some of the Kanji characters have several slightly different forms for the same meaning, but different usage. Alternative Kanjis have many names—“old forms” and “new forms”, “Gakusan” meaning educational purpose, or systematic names given by JIS (Japanese Industrial Standards).

There are a couple of reasons for using alternative Kanji. As written above, Kanji and Kana had a long journey of transformation over centuries, and while we transfer from analog manuscript, incunable, phototypesetting to digital font, some Kanji characters were accidentally drawn wrong, or developed in a few different forms, which ended up with alternative Kanji. In this case it’s mainly used for names of people or place, or on some publications they prefer the old letterform alternative Kanji on purpose. The Kanji 辺 has 23 alternatives in Adobe-Japan 1-6!

[IMAGE: Alternative Kanji of “hen” in 23 different ways]

Kanji letterforms in typefaces are not the same as how we hand-write; letterforms were optimized to make them fit for metal type designs. However, its simpler structures and elements are not the best to learn the anatomy of Kanji especially for learners. To resolve this, Japanese ministry of education is giving “curriculum guideline” to follow an alternative letterform, and it also includes very few Kana too. These alternative letterforms, sometimes called as _Gakusan style_, are designed with brush-like elements and expressions, which is also known as “humanistic style” in Latin. These design details allow readers to see more familiar Kanji forms and may enable children to learn Kanji more easily. 

[IMAGE: Alternative Kanji Gakusan examples]


## Tsume and Proportional Metrics (palt) 

Although Japanese fonts are designed full-width, some characters inevitably end up having more whitespace on both sides of the letter. This is because Japanese Kana used to be written vertically, so both the letter width and height varied back then. Therefore when typesetting, especially in the narrow textbox, the line would look jaggedly due to the inconsistent whitespace. To resolve this problem, Japanese typography uses its own setting called _Tsume_, in other words _Proportional Metrics_, instead of tracking or kerning. Tsume enables the font to tighten its typesetting. The difference between Tsume and Kerning is that Tsume shrinks the whitespace on both sides of the letter, while kerning goes in between two letters. Tsume values are defined by the type designers when designing the font, and users can’t set their own value. Some Japanese type foundries are updating their flagship fonts with Japanese kerning values in addition to the Tsume. Tracking is rarely used. “Betagumi” typesetting is also very popular—it means block typesetting with no Tsume or kerning.

[IMAGE: Difference of palt ON and OFF]  
