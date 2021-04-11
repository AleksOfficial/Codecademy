<?php #yey another mad lib

function generateStory($singular_noun,$verb,$color)
{
    $story = "The ${singular_noun}s are lovely, $color, and deep.\n
But I have promises to keep,\n
And miles to go before I $verb,\n
And miles to go before I $verb.";
return $story;

}
echo generateStory("mom","play","green");
echo generateStory("dad","slamdunk","black");
echo generateStory("kid","jump","red");
#that's it? .. oh dear. k
