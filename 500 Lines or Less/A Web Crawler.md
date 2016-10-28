# [A Web Crawler With asyncio Coroutines](http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html)

- [x] [Introduction]()
- [ ] [The Task]()
- [ ] [Introduction]()
- [ ] [Introduction]()
- [ ] [Introduction]()
- [ ] [Introduction]()

## Introduction

Classical computer science emphasizes efficient algorithms that complete computations as quickly as possible. But many networked programs spend their time not computing, but holding open many connections that are slow, or have infrequent events. These programs present a very different challenge: to wait for a huge number of network events efficiently. A contemporary approach to this problem is asynchronous I/O, or "async".

Classical computer science emphasizes efficient algorithms that complete computations as quickly as possible. 

>> computer science emphasizes efficient algorithms [that complete computations as quickly as possible]. 

    computer science emphasizes algorithms.

But many networked programs spend their time not computing, but holding open many connections that are slow, or have infrequent events.

>> But many networked programs spend their time not computing, 
>> but holding open many connections that are slow, or have infrequent events.

    programs spend time not computing

    connections are slow, or have infrequent events.

These programs present a very different challenge: to wait for a huge number of network events efficiently.

    challenge: wait for a huge events.

A contemporary approach to this problem is asynchronous I/O, or "async".

    using asynchoronous I/O.

---

This chapter presents a simple web crawler. The crawler is an archetypal async application because it waits for many responses, but does little computation. The more pages it can fetch at once, the sooner it completes. If it devotes a thread to each in-flight request, then as the number of concurrent requests rises it will run out of memory or other thread-related resource before it runs out of sockets. It avoids the need for threads by using asynchronous I/O.

This chapter presents a simple web crawler. 

    This chapter presents crawler.

The crawler is an archetypal async application because it waits for many responses, but does little computation. 

    crawler is application.

The more pages it can fetch at once, the sooner it completes. 

If it devotes a thread to each in-flight request, then as the number of concurrent requests rises it will run out of memory or other thread-related resource before it runs out of sockets. 

It avoids the need for threads by using asynchronous I/O.

    It avoids threads. Using asynchronous I/O.

---

We present the example in three stages. First, we show an async event loop and sketch a crawler that uses the event loop with callbacks: it is very efficient, but extending it to more complex problems would lead to unmanageable spaghetti code. Second, therefore, we show that Python coroutines are both efficient and extensible. We implement simple coroutines in Python using generator functions. In the third stage, we use the full-featured coroutines from Python's standard "asyncio" library1, and coordinate them using an async queue.

We present the example in three stages. 

- First, we show an async event loop and sketch a crawler that uses the event loop with callbacks: it is very efficient, but extending it to more complex problems would lead to unmanageable spaghetti code. 
- Second, therefore, we show that Python coroutines are both efficient and extensible. We implement simple coroutines in Python using generator functions. 
- Third stage, we use the full-featured coroutines from Python's standard "asyncio" library1, and coordinate them using an async queue.

- First, we show an async event loop and sketch a crawler that uses the event loop with callbacks: it is very efficient, but extending it to more complex problems would lead to unmanageable spaghetti code. 

    we show an async event loop and sketch a crawler [that uses the event loop with callbacks]:

    we show async event loop and sketch a crawler.

    crawler is uses the event loop with callbacks.

    it is efficient, 
    
    but extending it (to more complex) problems would lead (to unmanageable spaghetti code). 

- Second, therefore, we show that Python coroutines are both efficient and extensible. We implement simple coroutines in Python using generator functions. 

    we show that Python coroutines are both efficient and extensible. We implement simple coroutines in Python using generator functions. 

    we show that Python coroutines are both efficient and extensible. 

    we show Python coruthines. 
    
    Python coroutines are both efficient and extensible. 
    
    We implement simple coroutines (in Python using generator functions). 

    We implement simple coroutines.

- Third stage, we use the full-featured coroutines from Python's standard "asyncio" library1, and coordinate them using an async queue.

    we use the full-featured coroutines (from Python's standard "asyncio" library1, and coordinate them using an async queue).

    we use the full-featured coroutines.
