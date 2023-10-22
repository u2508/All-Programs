engineering={
    'subjects:':'maths,''physics,''chemistry,''computers',
    'years:':'4 or less than 4',
    'best institute in india:':'IIT Dehli',
    'most prestiious course:':'software devlopment',
    'preparation coachings:':'VMC ''FITJEE ''AKASH'
}
medical={
    'subjects:':'biology,''physics,''chemistry,''psychology',
    'years:':'more than 4',
    'best institute in india:':'AIIMS',
    'most prestiious course:':'neuro surgeon',
    'preparation coachings:':'AKASH'
}
admin_info={
    'Admin head:':'Utkarsh',
    'Offical Name:':'One Shot Op',
    'Mail id:':'utkarshgupta64825@gmail.com'
}
a=input('Enter stream for info :')
if a=='medical' or a=='Medical':
    for i in medical:
        print(i,medical[i])
elif a=='engineering' or a=='Engineering':
    for j in engineering:
        print(j,engineering[j])
elif a=='commerce' or a=='Commerce' or a=='Humanities' or a=='humanities':
    print('Not enough data to represent this info kindly contact admin.','\n''the admin info is as follows:')
    for k in admin_info:
        print(k,admin_info[k])
