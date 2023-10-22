VERSION 5.00
Begin VB.Form Form10 
   BackColor       =   &H00FF0000&
   Caption         =   "question7"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   BeginProperty Font 
      Name            =   "MS Reference Sans Serif"
      Size            =   26.25
      Charset         =   0
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form9"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "next question"
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
      Left            =   5160
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   9120
      Width           =   7695
   End
   Begin VB.OptionButton Option4 
      BackColor       =   &H00FF0000&
      Caption         =   "Starfish"
      Height          =   1455
      Left            =   11040
      TabIndex        =   4
      Top             =   7320
      Width           =   8655
   End
   Begin VB.OptionButton Option3 
      BackColor       =   &H00FF0000&
      Caption         =   "Blue Whale"
      Height          =   1335
      Left            =   840
      TabIndex        =   3
      Top             =   7440
      Width           =   8775
   End
   Begin VB.OptionButton Option2 
      BackColor       =   &H00FF0000&
      Caption         =   " Ganga River Dolpin"
      Height          =   1335
      Left            =   11040
      TabIndex        =   2
      Top             =   4680
      Width           =   8655
   End
   Begin VB.OptionButton Option1 
      BackColor       =   &H00FF0000&
      Caption         =   "Sea Horse"
      Height          =   1335
      Left            =   840
      TabIndex        =   1
      Top             =   4680
      Width           =   8775
   End
   Begin VB.Timer Timer1 
      Left            =   15720
      Top             =   11120
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
      Height          =   1575
      Left            =   8160
      TabIndex        =   8
      Top             =   840
      Width           =   615
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
      Height          =   1215
      Left            =   8640
      TabIndex        =   7
      Top             =   960
      Width           =   1455
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
      Height          =   1455
      Left            =   6840
      TabIndex        =   6
      Top             =   960
      Width           =   1455
   End
   Begin VB.Label Label1 
      BackColor       =   &H00FF0000&
      BackStyle       =   0  'Transparent
      Caption         =   " Q 7 . which of these was declared india's national  water animal in 2009 ?"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   27.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1335
      Left            =   120
      TabIndex        =   0
      Top             =   2400
      Width           =   19815
   End
End
Attribute VB_Name = "Form10"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a, b As Double

Private Sub Command1_Click()
Form10.Hide
Form11.Show
End Sub

Private Sub Form_Load()
Timer1.Enabled = True
Timer1.Interval = 10
a = 0
b = 0
End Sub
Private Sub Option2_Click()
If Option2 = True Then
MsgBox "correct answer"
End If
End Sub

Private Sub Option3_Click()
If Option3 = True Then
MsgBox "wrong answer"
End If
Form10.Hide
Form16.Show
End Sub

Private Sub Option4_Click()
If Option4 = True Then
MsgBox "wrong answer"
End If
Form10.Hide
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
