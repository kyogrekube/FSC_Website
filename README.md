# ITWS1100-S24-team12

Welcome to the RPI FSC website repo!

This project aims to provide students, parents, and others a single, accessible, and easy to use application
to find information on all of RPI's Greek Organizations. 

Technologies Used: HTML, JSON, JavaScript, CSS.

Current Features/Uses:
1. Landing and council pages provide information on Greek life eligibility requirements at RPI and other council info
2. Organization pages are loaded dynamically using the dataFill.js file, which will grab the needed information from
   greekInfo.json. This allows the information, links, images, and color schemes of each page to be accurate without having to change
   much HTML code
3. Easily modifiable through the greekInfo.json file!
   The greekInfo.json file contains all information on the greek organizations that exist on the RPI campus.
   Some bits of information due not apply to certain organizations, such as "letters" for Acacia, who do not
   have greek letters. Other information, such as "house_address", may not apply to a chapter at the moment,
   but need to be added in the future. In order to add this information, simply add the corresponding variable
   in its section. Currently, chapters without this information available simply do not have the variable created.
4. A interactive google map embed that allows users to find the chapter houses of IFC member organizations

Feature Features to implement:
1. Pages on current chapter leadership, FSC executive board, and FSC advisors
2. Philanthropy information
3. Tags that can be applied to each organization or council that can be utilized via a "Search" feature
4. Login for both admins (this would be for FSC executive board members) and member organizations (one per chapter)
5. Panhellenic Council Map (just like the one that exists for the IFC)

How to use this project:
1. Download the repo
2. Either run on your local machine using something akin to the "Show Preview" feature of Visual Studio Code
   or upload it to a server and interact with it there.

Link to Github Repo: https://github.com/RPI-ITWS/ITWS1100-S24-team12