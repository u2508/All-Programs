VERSION 5.00
Begin VB.Form Form8 
   BackColor       =   &H00FF0000&
   Caption         =   "question5"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   BeginProperty Font 
      Name            =   "MS Reference Sans Serif"
      Size            =   8.25
      Charset         =   0
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form7"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.Timer Timer1 
      Left            =   9840
      Top             =   5040
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "next question"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   27.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   855
      Left            =   10560
      MaskColor       =   &H00FF0000&
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   8160
      Width           =   4935
   End
   Begin VB.OptionButton Option4 
      BackColor       =   &H00FF0000&
      Caption         =   "Shikhar Dhawan"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   855
      Left            =   11160
      TabIndex        =   4
      Top             =   6600
      Width           =   7935
   End
   Begin VB.OptionButton Option3 
      BackColor       =   &H00FF0000&
      Caption         =   "Yuvraj Singh"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   855
      Left            =   1800
      TabIndex        =   3
      Top             =   6720
      Width           =   7455
   End
   Begin VB.OptionButton Option2 
      BackColor       =   &H00FF0000&
      Caption         =   "Virat kohli"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   855
      Left            =   11160
      TabIndex        =   2
      Top             =   3600
      Width           =   7935
   End
   Begin VB.OptionButton Option1 
      BackColor       =   &H00FF0000&
      Caption         =   "Mahendra Singh DHONI"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   855
      Left            =   1680
      TabIndex        =   1
      Top             =   3600
      Width           =   7455
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
      Left            =   8400
      TabIndex        =   8
      Top             =   720
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
      Height          =   1215
      Left            =   8760
      TabIndex        =   7
      Top             =   840
      Width           =   1335
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "00"
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
      Left            =   7320
      TabIndex        =   6
      Top             =   960
      Width           =   1215
   End
   Begin VB.Label Label1 
      BackColor       =   &H00FF0000&
      Caption         =   "Q5. Who has scored 36 runs in 1 over  in cricket ?"
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
      Left            =   240
      TabIndex        =   0
      Top             =   2040
      Width           =   19215
   End
End
Attribute VB_Name = "Form8"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a, b As Double
Private Sub Command1_Click()
Form8.Hide
Form9.Show
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
Form8.Hide
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
Form8.Hide
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
