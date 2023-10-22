VERSION 5.00
Begin VB.Form Form12 
   BackColor       =   &H00FF0000&
   Caption         =   "Q 9 ."
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   LinkTopic       =   "Form11"
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
      Height          =   1215
      Left            =   7200
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   9480
      Width           =   7455
   End
   Begin VB.OptionButton Option4 
      BackColor       =   &H00FF0000&
      Caption         =   "shakhl"
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
      Left            =   10080
      TabIndex        =   4
      Top             =   7440
      Width           =   9855
   End
   Begin VB.OptionButton Option3 
      BackColor       =   &H00FF0000&
      Caption         =   "Hola Mohalla"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1575
      Left            =   240
      TabIndex        =   3
      Top             =   7440
      Width           =   8655
   End
   Begin VB.OptionButton Option2 
      BackColor       =   &H00FF0000&
      Caption         =   "gatka"
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
      Left            =   10200
      TabIndex        =   2
      Top             =   5160
      Width           =   9735
   End
   Begin VB.OptionButton Option1 
      BackColor       =   &H00FF0000&
      Caption         =   "kakaar"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   240
      TabIndex        =   1
      Top             =   5280
      Width           =   8655
   End
   Begin VB.Timer Timer1 
      Enabled         =   0   'False
      Left            =   25000
      Top             =   8520
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
      Height          =   1335
      Left            =   9360
      TabIndex        =   8
      Top             =   1560
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
      Height          =   1335
      Left            =   9840
      TabIndex        =   7
      Top             =   1680
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
      Height          =   1215
      Left            =   8040
      TabIndex        =   6
      Top             =   1680
      Width           =   1455
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "Q 9 . Which of these is a traditional Sikh Maritial Art named after a stick used to practice sword fighting?"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   2175
      Left            =   120
      TabIndex        =   0
      Top             =   2880
      Width           =   19815
   End
End
Attribute VB_Name = "Form12"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a, b As Double

Private Sub Command1_Click()
Form12.Hide
Form13.Show

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
Form12.Hide
Form16.Show
End Sub

Private Sub Option4_Click()
If Option4 = True Then
MsgBox "wrong answer"
End If
Form12.Hide
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
