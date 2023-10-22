VERSION 5.00
Begin VB.Form Form13 
   BackColor       =   &H00FF0000&
   Caption         =   "Q 10."
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   BeginProperty Font 
      Name            =   "MS Reference Sans Serif"
      Size            =   48
      Charset         =   0
      Weight          =   400
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form12"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "next question"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   54.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   6960
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   8880
      Width           =   8415
   End
   Begin VB.OptionButton Option4 
      BackColor       =   &H00FF0000&
      Caption         =   "ipod"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1335
      Left            =   10920
      TabIndex        =   4
      Top             =   6720
      Width           =   9015
   End
   Begin VB.OptionButton Option3 
      BackColor       =   &H00FF0000&
      Caption         =   "blackberry"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   120
      TabIndex        =   3
      Top             =   6600
      Width           =   9615
   End
   Begin VB.OptionButton Option2 
      BackColor       =   &H00FF0000&
      Caption         =   "sony digital camera"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   10920
      TabIndex        =   2
      Top             =   4320
      Width           =   9015
   End
   Begin VB.OptionButton Option1 
      BackColor       =   &H00FF0000&
      Caption         =   "iphone"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   24
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   120
      TabIndex        =   1
      Top             =   4320
      Width           =   9615
   End
   Begin VB.Timer Timer1 
      Left            =   25240
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
      Height          =   1095
      Left            =   7800
      TabIndex        =   8
      Top             =   480
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
      Height          =   1455
      Left            =   8280
      TabIndex        =   7
      Top             =   600
      Width           =   1815
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
      Left            =   6480
      TabIndex        =   6
      Top             =   600
      Width           =   1455
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "Q 10. Curve Javelin, Storm and Bold are varieties of which of these instruments?"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   36
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1815
      Left            =   240
      TabIndex        =   0
      Top             =   1680
      Width           =   19815
   End
End
Attribute VB_Name = "Form13"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a, b As Double

Private Sub Command1_Click()
Form13.Hide
Form14.Show
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
Form13.Hide
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
Form13.Hide
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
