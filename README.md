{% include style.html %}
<head>
        <title>Home Page</title>
        <link rel="icon" type="image/x-icon" href="https://cdn3.iconfinder.com/data/icons/popular-services-brands/512/github-512.png">
</head>
<h2 style='text-align: center'>Search for Pages</h2>
<input autocomplete="off" style="margin-left: 30%; margin-right: 30%; font-size: 17.5px; height: 25px; width: 40%" type="text" id="SearchInput" onkeyup="SearchMain(list = websitePages, textcolor = 'white', nullcolor = '#e30202', SearchID = 'SearchInput', ResultID = 'SearchResult', DebugMode = false)" placeholder="Search for pages" title="Search for pages">
<br>
<p style="text-align: center" id="SearchResult"></p>
<script>
        // this is an array that includes most of our website's pages.
        // each object in the list has a name and a path.
        // the name will be checked against the user's input to check which object should be selected to return.
        // the path is used to create a link to the desired page
        let websitePages =
            [
                {"name":"Test Prep / Notes", "path":"https://dtsivkovski.github.io/dtsivkovski-cspt3/testPrep"},
                {"name":"Data Structures Project", "path":"https://dtsivkovski.github.io/dtsivkovski-cspt3/dsProject"},
                {"name":"Create Task", "path":"https://dtsivkovski.github.io/dtsivkovski-cspt3/createtask"},
                {"name":"Home", "path":"https://dtsivkovski.github.io/dtsivkovski-cspt3/"},
                {"name":"Guython", "path":"https://akhilnandhakumar.github.io/Guython/"},
                {"name":"Individual GitHub Repository", "path":"https://github.com/dtsivkovski/dtsivkovski-cspt3"},
                {"name":"Team GitHub Repository", "path":"https://github.com/LindaLiu1202/just_here_to_code/"},
                {"name":"Replit Project", "path":"https://replit.com/@DanielTsivkovsk/dtsivkovski-cspt3#python/tt0-menu.py"},
            ] ;

        function SearchMain(list = websitePages, textcolor = 'white', nullcolor = 'red', SearchID = 'SearchInput', ResultID = 'SearchResult', DebugMode = false, NoRText = 'No Results') {
            let input = document.getElementById(SearchID);
            let filter = input.value.toUpperCase(); // the user's input is changed to uppercase so that the search is not case-sensitive
            document.getElementById(ResultID).innerHTML = '| ' // this line makes the output blank whenever the function is called so that previous information is removed
            if (DebugMode === false) {
                for (x = 0; x < list.length; x++) { // this section goes through the items in my array and checks if the user's input is the same as any object name
                    if (list[x].name.toUpperCase().includes(filter)) { //using include function allows users to only input part of the page name instead of the whole thing
                        let link = list[x].path;
                        let title = list[x].name;
                        let output = `<a target="_blank" class='intlink' href='${link}'>${title}</a>` + ' | '; //this allows multiple links to be included in the result
                        document.getElementById(ResultID).innerHTML += output
                        document.getElementById(ResultID).style.color = 'grey'
                        let intlink = document.getElementsByClassName('intlink')
                        for (y = 0; y < intlink.length; y++) {
                            intlink[y].style.color = textcolor
                        }
                    }
                    if (filter === '') { //in case the user leaves the input blank, this statements causes the function to return "No Results"
                        document.getElementById(ResultID).innerHTML = NoRText
                        document.getElementById(ResultID).style.color = nullcolor
                    }
                }
            }
            else {
                for (i = 0; i < list.length; i++) {
                    let link = list[i].path
                    let title = list[i].name
                    let output = `<a href='${link}'>${title}</a>` + ' | ' //this allows multiple links to be included in the result
                    document.getElementById(ResultID).innerHTML += output
                    document.getElementById(ResultID).style.color = textcolor
                }
                document.getElementById(ResultID).innerHTML += '<br>' + `<p id='NoRText'>${NoRText}</p>`
                document.getElementById('NoRText').style.color = nullcolor
                }
        }
</script>


![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/89223402/157379234-9fe32df4-8000-4f0b-88aa-4c279c25001e.gif)

<!-- <table>
    <tr>
        <td><a href="https://dtsivkovski.github.io/dtsivkovski-cspt3/">Main</a></td>
        <td><a href="https://dtsivkovski.github.io/dtsivkovski-cspt3/dsProject">Data Structures Project</a></td>
        <td><a href="https://dtsivkovski.github.io/dtsivkovski-cspt3/testPrep">Test Prep / Notes</a></td>
        <td><a href="https://dtsivkovski.github.io/dtsivkovski-cspt3/createtask">Create Task</a></td>
    </tr>
</table>
<hr> -->

# Daniel Tsivkovski's Github Page

- [[Link to individual repo]](https://github.com/dtsivkovski/dtsivkovski-cspt3)
- [[Link to team repo]](https://github.com/LindaLiu1202/just_here_to_code/)

## Timebox (Newest First)

#### Week 2 - [[Review Ticket]](https://github.com/dtsivkovski/dtsivkovski-cspt3/issues/3)
- [5.5-5.6 Notes + Actions](https://dtsivkovski.github.io/dtsivkovski-cspt3/notes/5.5-5.6)
- [Week 2 Technicals](https://dtsivkovski.github.io/dtsivkovski-cspt3/dsProject)

#### Week 1 - [[Review Ticket]](https://github.com/dtsivkovski/dtsivkovski-cspt3/issues/2)
- [5.3-5.4 Notes + Actions](https://dtsivkovski.github.io/dtsivkovski-cspt3/notes/5.3-5.4)
- [Week 1 Technicals](https://dtsivkovski.github.io/dtsivkovski-cspt3/dsProject)
- [Populated Create Task Page](https://dtsivkovski.github.io/dtsivkovski-cspt3/createtask)

#### Week 0 - [[Review Ticket]](https://github.com/dtsivkovski/dtsivkovski-cspt3/issues/1)
- [TT0 - Python Menu](https://dtsivkovski.github.io/dtsivkovski-cspt3/dsProject) 
- [5.1-5.2 Notes + Actions](https://dtsivkovski.github.io/dtsivkovski-cspt3/notes/5.1-5.2)
   
