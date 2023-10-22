VERSION 5.00
Begin VB.Form Form22 
   BackColor       =   &H000000FF&
   Caption         =   "CLASS 11 FEE STRUCTURE"
   ClientHeight    =   10950
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   20250
   BeginProperty Font 
      Name            =   "Matura MT Script Capitals"
      Size            =   110.25
      Charset         =   0
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form1"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command3 
      BackColor       =   &H00FF0000&
      Caption         =   "credits"
      Height          =   2145
      Left            =   12360
      Style           =   1  'Graphical
      TabIndex        =   27
      TabStop         =   0   'False
      Top             =   8040
      Width           =   7695
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00FF0000&
      Caption         =   "exit"
      Height          =   2085
      Left            =   12480
      Style           =   1  'Graphical
      TabIndex        =   26
      Top             =   5520
      Width           =   7095
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "CALCULATE"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   39.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1335
      Left            =   12240
      Style           =   1  'Graphical
      TabIndex        =   25
      Top             =   3720
      Width           =   7815
   End
   Begin VB.TextBox FEE 
      BackColor       =   &H00FF0000&
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1935
      Left            =   6360
      TabIndex        =   24
      Top             =   8160
      Width           =   5535
   End
   Begin VB.CheckBox SUB5H 
      BackColor       =   &H00FF0000&
      Caption         =   "ECO, PE, IP, CS (RS. 300)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   9000
      TabIndex        =   22
      Top             =   7320
      Width           =   2895
   End
   Begin VB.CheckBox SUB5S 
      BackColor       =   &H00FF0000&
      Caption         =   "BIO, PE, CS, COMM. ART, SOCIO, PSYCHO (RS. 300)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   360
      TabIndex        =   21
      Top             =   7320
      Width           =   2415
   End
   Begin VB.CheckBox SUB4H 
      BackColor       =   &H00FF0000&
      Caption         =   "PSYCHO, SOCIO, ECO, PE (RS. 250)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   9000
      TabIndex        =   20
      Top             =   6480
      Width           =   3015
   End
   Begin VB.CheckBox SUB3H 
      BackColor       =   &H00FF0000&
      Caption         =   "POL. SCIENCE (RS. 200) "
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   9000
      TabIndex        =   19
      Top             =   5760
      Width           =   2775
   End
   Begin VB.CheckBox SUB2H 
      BackColor       =   &H00FF0000&
      Caption         =   "HISTORY, GEO (RS. 150)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   9000
      TabIndex        =   18
      Top             =   5040
      Width           =   2655
   End
   Begin VB.CheckBox SUB1H 
      BackColor       =   &H00FF0000&
      Caption         =   "ENGLISH (RS. 100)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   9000
      TabIndex        =   17
      Top             =   4320
      Width           =   2655
   End
   Begin VB.CheckBox SUB5C 
      BackColor       =   &H00FF0000&
      Caption         =   "MATHS, PE, SOCIO, PSYCHO, COMM. ART, IP (RS. 300)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   675
      Left            =   4320
      TabIndex        =   15
      Top             =   7320
      Width           =   2775
   End
   Begin VB.CheckBox SUB4C 
      BackColor       =   &H00FF0000&
      Caption         =   "ECO (RS. 250)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   4320
      TabIndex        =   14
      Top             =   6480
      Width           =   2655
   End
   Begin VB.CheckBox SUB3C 
      BackColor       =   &H00FF0000&
      Caption         =   "BST (RS. 200) "
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   4320
      TabIndex        =   13
      Top             =   5760
      Width           =   2655
   End
   Begin VB.CheckBox SUB2C 
      BackColor       =   &H00FF0000&
      Caption         =   "ACCOUNTS (RS. 150)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   4320
      TabIndex        =   12
      Top             =   5040
      Width           =   2655
   End
   Begin VB.CheckBox SUB1C 
      BackColor       =   &H00FF0000&
      Caption         =   "ENGLISH (RS. 100)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   4320
      TabIndex        =   11
      Top             =   4320
      Width           =   2655
   End
   Begin VB.CheckBox SUB4S 
      BackColor       =   &H00FF0000&
      Caption         =   "MATHS, PE, CS, COMM. ART, SOCIO, PSYCHO (RS. 250)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   360
      TabIndex        =   9
      Top             =   6480
      Width           =   2775
   End
   Begin VB.CheckBox SUB3S 
      BackColor       =   &H00FF0000&
      Caption         =   "CHEMISTRY (RS. 200) "
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   360
      TabIndex        =   8
      Top             =   5760
      Width           =   2415
   End
   Begin VB.CheckBox SUB2S 
      BackColor       =   &H00FF0000&
      Caption         =   "PHYSICS (RS. 150)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   360
      TabIndex        =   7
      Top             =   5040
      Width           =   2415
   End
   Begin VB.CheckBox SUB1S 
      BackColor       =   &H00FF0000&
      Caption         =   "ENGLISH (RS. 100)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   360
      TabIndex        =   6
      Top             =   4320
      Width           =   2415
   End
   Begin VB.OptionButton H 
      BackColor       =   &H00FF0000&
      Caption         =   "HUMANITIES (RS. 4000)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   5760
      TabIndex        =   4
      Top             =   2400
      Width           =   2295
   End
   Begin VB.OptionButton C 
      BackColor       =   &H00FF0000&
      Caption         =   "COMMERCE (RS. 3000)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   3000
      TabIndex        =   2
      Top             =   2400
      Width           =   2295
   End
   Begin VB.OptionButton S 
      BackColor       =   &H00FF0000&
      Caption         =   "SCIENCE (RS. 2000)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   720
      TabIndex        =   1
      Top             =   2400
      Width           =   1815
   End
   Begin VB.Label Label6 
      BackStyle       =   0  'Transparent
      Caption         =   "TOTAL FEE"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   3360
      TabIndex        =   23
      Top             =   8280
      Width           =   3135
   End
   Begin VB.Label Label5 
      BackStyle       =   0  'Transparent
      Caption         =   "SUBJECTS (HUMANITIES)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   9.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   9000
      TabIndex        =   16
      Top             =   3480
      Width           =   3135
   End
   Begin VB.Label Label4 
      BackStyle       =   0  'Transparent
      Caption         =   "SUBJECTS (COMMERCE)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   9.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   4440
      TabIndex        =   10
      Top             =   3480
      Width           =   2895
   End
   Begin VB.Label Label3 
      BackStyle       =   0  'Transparent
      Caption         =   "SUBJECTS (SCIENCE)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   9.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   360
      TabIndex        =   5
      Top             =   3480
      Width           =   2655
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "STREAM"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   18
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   1200
      TabIndex        =   3
      Top             =   1680
      Width           =   2655
   End
   Begin VB.Label Label1 
      Alignment       =   2  'Center
      BackStyle       =   0  'Transparent
      Caption         =   "CLASS 11 FEE STRUCTURE"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1335
      Left            =   600
      TabIndex        =   0
      Top             =   240
      Width           =   18495
   End
End
Attribute VB_Name = "Form22"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
If S = True Then
STREAMRATE = 2000
End If
If C = True Then
STREAMRATE = 3000
End If
If H = True Then
STREAMRATE = 4000
End If
SUBJECTRATE = 0
If SUB1S = 1 Then
SUBJECTRATE = SUBJECTRATE + 100
End If
If SUB2S = 1 Then
SUBJECTRATE = SUBJECTRATE + 150
End If
If SUB3S = 1 Then
SUBJECTRATE = SUBJECTRATE + 200
End If
If SUB4S = 1 Then
SUBJECTRATE = SUBJECTRATE + 250
End If
If SUB5S = 1 Then
SUBJECTRATE = SUBJECTRATE + 300
End If
If SUB1C = 1 Then
SUBJECTRATE = SUBJECTRATE + 100
End If
If SUB2C = 1 Then
SUBJECTRATE = SUBJECTRATE + 150
End If
If SUB3C = 1 Then
SUBJECTRATE = SUBJECTRATE + 200
End If
If SUB4C = 1 Then
SUBJECTRATE = SUBJECTRATE + 250
End If
If SUB5C = 1 Then
SUBJECTRATE = SUBJECTRATE + 300
End If
If SUB1H = 1 Then
SUBJECTRATE = SUBJECTRATE + 100
End If
If SUB2H = 1 Then
SUBJECTRATE = SUBJECTRATE + 150
End If
If SUB3H = 1 Then
SUBJECTRATE = SUBJECTRATE + 200
End If
If SUB4H = 1 Then
SUBJECTRATE = SUBJECTRATE + 250
End If
If SUB5H = 1 Then
SUBJECTRATE = SUBJECTRATE + 300
End If
ANS = (STREAMRATE + SUBJECTRATE)
FEE.Text = Str$(ANS)
End Sub

Private Sub Command2_Click()
End
End Sub

Private Sub Command3_Click()
Form23.Show
Form22.Hide
End Sub
