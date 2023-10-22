VERSION 5.00
Begin VB.Form Form11 
   BackColor       =   &H00FF0000&
   Caption         =   "question 8"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   BeginProperty Font 
      Name            =   "MS Reference Sans Serif"
      Size            =   27.75
      Charset         =   0
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form10"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "next question"
      Height          =   975
      Left            =   11400
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   9960
      Width           =   7815
   End
   Begin VB.OptionButton Option4 
      BackColor       =   &H00FF0000&
      Caption         =   "light"
      Height          =   1575
      Left            =   10920
      TabIndex        =   4
      Top             =   7800
      Width           =   9135
   End
   Begin VB.OptionButton Option3 
      BackColor       =   &H00FF0000&
      Caption         =   "lion"
      Height          =   1455
      Left            =   240
      TabIndex        =   3
      Top             =   7800
      Width           =   9375
   End
   Begin VB.OptionButton Option2 
      BackColor       =   &H00FF0000&
      Caption         =   "father"
      Height          =   1530
      Left            =   10920
      TabIndex        =   2
      Top             =   4680
      Width           =   9015
   End
   Begin VB.OptionButton Option1 
      BackColor       =   &H00FF0000&
      Caption         =   "gold"
      Height          =   1455
      Left            =   240
      TabIndex        =   1
      Top             =   4680
      Width           =   9375
   End
   Begin VB.Timer Timer1 
      Left            =   15480
      Top             =   14000
   End
   Begin VB.Label Label4 
      BackStyle       =   0  'Transparent
      Caption         =   ":"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   54.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   8040
      TabIndex        =   8
      Top             =   960
      Width           =   735
   End
   Begin VB.Label Label3 
      BackStyle       =   0  'Transparent
      Caption         =   "00"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   54.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1335
      Left            =   8400
      TabIndex        =   7
      Top             =   1080
      Width           =   1575
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "00"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   54.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   6720
      TabIndex        =   6
      Top             =   1080
      Width           =   1575
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   " Q 8 . What does Kesari mean in 'Punjab Kesari' - a popular title of Lala Lajpat Rai?"
      Height          =   1695
      Left            =   120
      TabIndex        =   0
      Top             =   2280
      Width           =   19815
   End
End
Attribute VB_Name = "Form11"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a, b As Double

Private Sub Command1_Click()
Form11.Hide
Form12.Show
End Sub

Private Sub Form_Load()
Timer1.Enabled = True
Timer1.Interval = 10
a = 0
b = 0
End Sub
Private Sub Option2_Click()
If Option2 = True Then
MsgBox "wrong answer"
End If
Form11.Hide
Form16.Show
End Sub

Private Sub Option3_Click()
If Option3 = True Then
MsgBox "correct answer"
End If
End Sub

Private Sub Option4_Click()
If Option4 = True Then
MsgBox "wrong answer"
End If
Form11.Hide
Form16.Show
End Sub

Private Sub Timer1_Timer()
a = a + 1
Me.Label3.Caption = a
If a = 60 Then
a = 0
b = b + 1
Me.Label2.Caption = b
End If
If b = 60 Then
Timer1.Enabled = False
MsgBox "time is up"
End If

End Sub
