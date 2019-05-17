def make_instruction_verify(group_type):
	instructions="<h1>Introduction</h1><p>We are doing a study on the best way to explain the choices given by \
	our group recommendation system to users.</p><p>Imagine you are planning a trip with your "+group_type+". You decide \
	to use a recommender system to select the order of 10 places/Points of Interest(POI) you want to visit in a city. You\
	 will be provided with your list of preferences and the sequence of places that the system has recommended you to visit. \
	 Each preference has been given a rating from 1 to 10, 1 being the least liked and 10 being the most liked.</p><hr><h1>Steps</h1><ol>\
	 	<li>Have a look at your likes and dislikes in the given preferences list.</li>	<li>Have a look at the sequence our system has \
	 	recommended your "+group_type+" to visit.</li>	<li>Read the explanation given for the sequence generated.</li>	<li>Select the option \
	 	that you like the most.</li></ol><hr><h1>Rules &amp; Tips</h1><ul>	<li>Point of Interest is also referred to by the short\
	 	 form, POI.</li>	<li>To write the comment in the box is not mandatory.</li></ul><p>	<br></p><hr><h1>Example</h1><p>Answer\
	 	  in the text box:</p><p>Out of these three sentence I choose the first one because it is more clear.</p><hr>"

	return instructions


def make_instruction_fid_fix(group_type):
	instructions="<h1>Introduction</h1><p>We are doing a study on the best way to explain the choices given by our group recommendation \
	system to users and whether the explanations provided by our system can be improved.&nbsp;</p><p>Imagine you are planning a trip with\
	 your "+group_type+". You decide to use a recommender system to select the order of 10 places/Points of Interest(POI) you want to visit in a \
	 city. You will be provided with your list of preferences and the sequence of places that the system has recommended you to visit. Each\
	  preference has been given a rating from 1 to 10, 1 being the least liked and 10 being the most liked.</p><hr><h1>Steps</h1><ol><li>\
	  Have a look at your likes and dislikes in the given preferences list.</li><li>Have a look at the sequence our system has recommended\
	   your "+group_type+" to visit.</li><li>Read the explanation given for the sequence generated.</li><li>In the following questions, choose whether\
	    you like or dislike the sentence.</li><li>If you dislike it, select the \"I do not like it\" option (text-box will appear below) and \
	    rewrite the sentence in your desired way, or delete it altogether by simply writing a dash(-).</li><li>If you like it, select the \
	    \"I like it\" option and move on to the next question.</li></ol><hr><h1>Rules &amp; Tips</h1><p>Point of Interest is also referred to\
	     by the short form, POI.</p><p>What to look for in a sentence:</p><ul><li>Style, is the sentence well written? Or could the English\
	      be improved?</li><li>Specificity, is the sentence specific enough? Or is it missing important details?</li><li>Any other improvements\
	       that come to mind</li><li>If you would like to completely change a particular sentence, feel free to do so!</li></ul><hr><h1>\
	       Example</h1><p>Sentence: I am going to drink some coffee right now.</p><p>Suppose, for example, you do not like this sentence \
	       and would like to change it, then you could write:</p><p>Answer: I am going to drink a glass of milk now.</p><p>Another possible\
	        option, if you do not like the sentence at all, or believe it does not fit in the explanation, is:</p><p>Answer: -</p><hr>"
	return instructions