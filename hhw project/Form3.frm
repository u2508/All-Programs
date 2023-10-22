VERSION 5.00
Begin VB.Form Form4 
   BackColor       =   &H00FF0000&
   Caption         =   "question 1"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   LinkTopic       =   "Form3"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.Timer Timer1 
      Left            =   7200
      Top             =   4080
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "next question"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   7680
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   6960
      Width           =   2535
   End
   Begin VB.OptionButton Option4 
      BackColor       =   &H00FF0000&
      Caption         =   "respect"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   8640
      TabIndex        =   4
      Top             =   5160
      Width           =   5055
   End
   Begin VB.OptionButton Option3 
      BackColor       =   &H00FF0000&
      Caption         =   "nothing"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   1920
      TabIndex        =   3
      Top             =   5160
      Width           =   4575
   End
   Begin VB.OptionButton Option2 
      BackColor       =   &H00FF0000&
      Caption         =   "garbage"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   8640
      TabIndex        =   2
      Top             =   3600
      Width           =   5055
   End
   Begin VB.OptionButton Option1 
      BackColor       =   &H00FF0000&
      Caption         =   "poison"
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   1920
      TabIndex        =   1
      Top             =   3600
      Width           =   4575
   End
   Begin VB.Label Label3 
      BackColor       =   &H00FF0000&
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
      Left            =   8760
      TabIndex        =   7
      Top             =   480
      Width           =   1575
   End
   Begin VB.Label Label2 
      BackColor       =   &H00FF0000&
      Caption         =   "00"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   54
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1335
      Left            =   5400
      TabIndex        =   6
      Top             =   480
      Width           =   2175
   End
   Begin VB.Label Label1 
      BackColor       =   &H00FF0000&
      Caption         =   "Q1.what is the thing which poor people have , rich people need it , if they eat it they  die."
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   18
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   975
      Left            =   1200
      TabIndex        =   0
      Top             =   1920
      Width           =   12975
   End
End
Attribute VB_Name = "Form4"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a, b As Double

Private Sub Command1_Click()
Form4.Hide
Form5.Show
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
Form4.Hide
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
Form4.Hide
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
