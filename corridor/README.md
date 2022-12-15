For this question, we first come through the image of corridor with each door associated with a hex.
Looking at the description, the hex seems to be a hash.
First I carved out all the hashes out by writing carvehash.py and output the hashes into carves-res.txt
Then I copied and pasted them into crackstation. It looks like these hashes are from 1 to 13 in md5 format.
From the description, we know we want to go back to the beginning, so 0 is the most probable number.
But just in case, I wrote customenumerator.py iterated from 0 to 50 converting the numbers to hash.
It did turn out the result is 0 in md5 format.
Appending it to the end of the given ip, we get the flag.

