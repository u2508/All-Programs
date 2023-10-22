a={
    'animes to be seen':'\n1.Naruto\n''2.Death Parade\n''3.No Game No Life\n',
    'songs to be listened':'\n1.Euphoria\n''2.Dynamite\n''3.Death Bed\n''4.Savage Love\n''5.Playdate\n''6.Can We Kiss Forever',
    'videos to be posted':'\n1.Alan Walker Best Top 3 Songs\n''2.Songs Be Listened Remix\n''3.Gaming Video\n''4.Roast On Insta Reels'
}
b=input('enter a key from objects(animes to be seen,songs to be listened,videos to be posted):- ')
print('The',b,'are :-',a.get(b,'key not found'),end='\n')
