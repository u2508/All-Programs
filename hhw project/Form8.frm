VERSION 5.00
Begin VB.Form Form9 
   BackColor       =   &H00FF0000&
   Caption         =   "question6"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   LinkTopic       =   "Form8"
   LockControls    =   -1  'True
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
      Height          =   1575
      Left            =   10200
      Style           =   1  'Graphical
      TabIndex        =   9
      Top             =   8640
      Width           =   8055
   End
   Begin VB.OptionButton Option4 
      BackColor       =   &H00FF0000&
      Caption         =   " J J Thompson, George Paget Thompson"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   11040
      TabIndex        =   8
      Top             =   6600
      Width           =   7215
   End
   Begin VB.OptionButton Option3 
      BackColor       =   &H00FF0000&
      Caption         =   "Herman Emil Fischer, Hans Fischer"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   840
      TabIndex        =   4
      Top             =   6720
      Width           =   7935
   End
   Begin VB.OptionButton Option2 
      BackColor       =   &H00FF0000&
      Caption         =   " Neils Bohr, Agge Bohr"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   11040
      TabIndex        =   3
      Top             =   3840
      Width           =   7215
   End
   Begin VB.OptionButton Option1 
      BackColor       =   &H00FF0000&
      Caption         =   " Marie Curie and Irene Curie"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   960
      TabIndex        =   2
      Top             =   3960
      Width           =   7815
   End
   Begin VB.Timer Timer1 
      Left            =   20280
      Top             =   8520
   End
   Begin VB.Label Label5 
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
      Height          =   1455
      Left            =   7680
      TabIndex        =   7
      Top             =   360
      Width           =   615
   End
   Begin VB.Label Label4 
      BackStyle       =   0  'Transparent
      Caption         =   "00"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   50.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   8160
      TabIndex        =   6
      Top             =   480
      Width           =   1335
   End
   Begin VB.Label Label3 
      BackStyle       =   0  'Transparent
      Caption         =   "00"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   50.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Index           =   1
      Left            =   6360
      TabIndex        =   5
      Top             =   480
      Width           =   1335
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "Q 6. Which of the following is not a pair of parent and child, who have both won Nobel Prize?"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1695
      Index           =   0
      Left            =   120
      TabIndex        =   1
      Top             =   1560
      Width           =   20055
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Height          =   1455
      Index           =   0
      Left            =   120
      TabIndex        =   0
      Top             =   1440
      Visible         =   0   'False
      Width           =   20055
   End
End
Attribute VB_Name = "Form9"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a, b As Double

Private Sub Command1_Click()
Form9.Hide
Form10.Show
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
Form15.Show
End Sub

Private Sub Option3_Click()
If Option3 = True Then
MsgBox "wrong answer"
End If
Form8.Hide
Form15.Show
End Sub

Private Sub Option4_Click()
If Option4 = True Then
MsgBox "correct answer"
End If
End Sub

Private Sub Timer1_Timer()
a = a + 1
Me.Label4.Caption = a
If a = 60 Then
a = 0
b = b + 1
Me.Label3(1).Caption = b
End If
If b = 60 Then
Timer1.Enabled = False
MsgBox "time is up"
End If
End Sub
