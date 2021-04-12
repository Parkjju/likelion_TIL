# HTML[1]

-   HTML이란? (Hyper Text = Link) + Markup Language

    -   markup language - 프로그래밍 언어와는 다름
    -   문서를 browser를 통해 서버로 보냄.
    -   브라우저상에 보이는 대로 서버가 데이터를 받는가? -> 서버가 이해할 수 있도록 컨텐츠에 대한 표기

-   구성요소
    1. 글
    2. 태그
    3. 속성
-   [Introduction to html 완주하기](www.codecademy.com)

-   codecademy Introduction to html 실습코드

```html
<body>
    <h1>The Brown Bear</h1>
    <div id="introduction">
        <h2>About Brown Bears</h2>
        <p>
            The brown bear (<em>Ursus arctos</em>) is native to parts of
            northern Eurasia and North America. Its conservation status is
            currently <strong>Least Concern</strong>.<br /><br />
            There are many subspecies within the brown bear species, including
            the Atlas bear and the Himalayan brown bear.
        </p>
        <h3>Species</h3>
        <ul>
            <li>Arctos</li>
            <li>Collarus</li>
            <li>Horribilis</li>
            <li>Nelsoni (extinct)</li>
        </ul>
        <h3>Features</h3>
        <p>
            Brown bears are not always completely brown. Some can be reddish or
            yellowish. They have very large, curved claws and huge paws. Male
            brown bears are often 30% larger than female brown bears. They can
            range from 5 feet to 9 feet from head to toe.
        </p>
    </div>
    <div id="habitat">
        <h2>Habitat</h2>
        <h3>Countries with Large Brown Bear Populations</h3>
        <ol>
            <li>Russia</li>
            <li>United States</li>
            <li>Canada</li>
        </ol>
        <h3>Countries with Small Brown Bear Populations</h3>
        <p>
            Some countries with smaller brown bear populations include Armenia,
            Belarus, Bulgaria, China, Finland, France, Greece, India, Japan,
            Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.
        </p>
    </div>
    <div id="media">
        <h2>Media</h2>
        <img
            src="https://content.codecademy.com/courses/web-101/web101-image_brownbear.jpg"
            alt="A Brown Bear"
        />
        <video
            src="https://content.codecademy.com/courses/freelance-1/unit-1/lesson-2/htmlcss1-vid_brown-bear.mp4"
            width="320"
            height="240"
            controls
        >
            Video not supported
        </video>
    </div>
</body>
```
