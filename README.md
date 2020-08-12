Task #1 : Getting to Philosophy
	In this task it was required to check the validity of getting the philosophy law using an automated script.
 Picking the right library
	Python offers a range of web scraping liberties and tools the most well known of which are requests, selenium, beautiful soup and scrapy. 
For the purpose of this project beautiful soup and requests  were considered the most appropriate. For scrapy is  a command line based tool and would not provide the required automation. Whereas selenium requires installing a webdriver which would make the code less portable.

Finding normal links
Normal links are links in an article body that redirect to another existing Wikipedia article. Generally speaking, there are 3 types of links in Wikipedia articles’ body, normal links, external links,red links that represent topics that do not on Wikipedia. 
Getting the first link: 
	The first thing the code does is to get the main body of any wikipedia page using the body’s id through a function (getArticleBody) that also saves the article url to an array that keeps track of all the pages visited. Once the body is  retrieved, a function (goToNextPage) loops over all the <a> tags and check whether the link is normal or not. This is done through a series of conditional statements: 
Check if link is external (all external links have a class attribute that indicates so)
Check if it is a self-link, it is a rare case but exists, (Like external links, self-links are distinguished by a class)
Check if it is a red link (all red links have the phrase (page does not exist)) in the title.
If all the above conditions are met, that means the link is indeed normal and the function redirects to it. If the function loops over all the article body and does not direct anywhere, it returns a boolean variable that indicates that a page with no links has been reached.

Main Program:
	An initial url to any wikipedia article is passed to the program. The program then chacks that this link is not to philosophy, has not been already visited before in this session, and does have links through a while loop. The loop keeps navigating the first link in each page until it either:
Reaches philosophy 
Reach a page with no links 
Reach a page that already exists in the history array 
The script  prints a message informing the user of which scenario had taken place.
