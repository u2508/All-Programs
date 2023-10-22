VERSION 5.00
Begin VB.Form Form5 
   BackColor       =   &H00FF0000&
   Caption         =   "QUESTION 2"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   LinkTopic       =   "Form4"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.Timer Timer1 
      Left            =   9840
      Top             =   5520
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "next question"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   11400
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   8280
      Width           =   3255
   End
   Begin VB.OptionButton Option4 
      BackColor       =   &H00FF0000&
      Caption         =   "mirror"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   855
      Left            =   11400
      TabIndex        =   4
      Top             =   6960
      Width           =   5295
   End
   Begin VB.OptionButton Option3 
      BackColor       =   &H00FF0000&
      Caption         =   "a bottle"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   855
      Left            =   3960
      TabIndex        =   3
      Top             =   7080
      Width           =   5055
   End
   Begin VB.OptionButton Option2 
      BackColor       =   &H00FF0000&
      Caption         =   "a horse"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   855
      Left            =   11280
      TabIndex        =   2
      Top             =   4680
      Width           =   6735
   End
   Begin VB.OptionButton Option1 
      BackColor       =   &H00FF0000&
      Caption         =   "a ghost"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   855
      Left            =   3960
      TabIndex        =   1
      Top             =   4440
      Width           =   5055
   End
   Begin VB.Label Label4 
      BackColor       =   &H00FF0000&
      Caption         =   " :"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   8400
      TabIndex        =   8
      Top             =   960
      Width           =   975
   End
   Begin VB.Label Label3 
      BackColor       =   &H00FF0000&
      Caption         =   "00"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   69.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   9360
      TabIndex        =   7
      Top             =   960
      Width           =   1815
   End
   Begin VB.Label Label2 
      BackColor       =   &H00FF0000&
      Caption         =   "00"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   69.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1575
      Left            =   6600
      TabIndex        =   6
      Top             =   960
      Width           =   1815
   End
   Begin VB.Label Label1 
      BackColor       =   &H00FF0000&
      Caption         =   "Q2. what has a neck but  no head? "
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   975
      Left            =   2760
      TabIndex        =   0
      Top             =   2640
      Width           =   13935
   End
End
Attribute VB_Name = "Form5"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a, b As Double

Private Sub Command1_Click()
Form6.Show
Form5.Hide
End Sub

Private Sub Form_Load()
Timer1.Enabled = True
Timer1.Interval = 10
a = 0
b = 0
End Sub


Private Sub Option1_Click()

End Sub

Private Sub Option2_Click()
If Option2 = True Then
MsgBox "wrong answer"
End If
Form5.Hide
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
Form5.Hide
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
If b = 30 Then
Timer1.Enabled = False
MsgBox "time is up"
End If
End Sub
