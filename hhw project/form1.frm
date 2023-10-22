VERSION 5.00
Begin VB.Form form1 
   BackColor       =   &H00FF0000&
   Caption         =   "login"
   ClientHeight    =   10395
   ClientLeft      =   120
   ClientTop       =   585
   ClientWidth     =   20250
   BeginProperty Font 
      Name            =   "MS Reference Sans Serif"
      Size            =   48
      Charset         =   0
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form1"
   ScaleHeight     =   10395
   ScaleWidth      =   20250
   Begin VB.TextBox Text1 
      BackColor       =   &H00FF0000&
      Height          =   1305
      Left            =   9120
      TabIndex        =   3
      Top             =   3600
      Width           =   8175
   End
   Begin VB.Frame Frame1 
      BackColor       =   &H00FF0000&
      Height          =   8175
      Left            =   2640
      TabIndex        =   1
      Top             =   1920
      Width           =   15375
      Begin VB.CommandButton login 
         BackColor       =   &H00FF0000&
         Caption         =   "click to login"
         Height          =   1185
         Left            =   3120
         Style           =   1  'Graphical
         TabIndex        =   8
         Top             =   6720
         Width           =   9975
      End
      Begin VB.CommandButton Command2 
         BackColor       =   &H00FF0000&
         Caption         =   "hide password"
         Height          =   1185
         Left            =   7920
         Style           =   1  'Graphical
         TabIndex        =   7
         Top             =   5280
         Width           =   7335
      End
      Begin VB.CommandButton Command1 
         BackColor       =   &H00FF0000&
         Caption         =   "show password"
         Height          =   1185
         Left            =   120
         Style           =   1  'Graphical
         TabIndex        =   6
         Top             =   5280
         Width           =   7695
      End
      Begin VB.TextBox Text2 
         BackColor       =   &H00FF0000&
         Height          =   1455
         Left            =   6480
         TabIndex        =   5
         Top             =   3360
         Width           =   8175
      End
      Begin VB.Label Label2 
         BackStyle       =   0  'Transparent
         Caption         =   "password:-"
         Height          =   1335
         Left            =   360
         TabIndex        =   4
         Top             =   3360
         Width           =   5895
      End
      Begin VB.Label Label1 
         BackStyle       =   0  'Transparent
         Caption         =   "username:-"
         Height          =   1215
         Left            =   360
         TabIndex        =   2
         Top             =   1440
         Width           =   6135
      End
   End
   Begin VB.Label Label3 
      BackColor       =   &H00FF0000&
      BackStyle       =   0  'Transparent
      Caption         =   "LOGIN DATABASE"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   66
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   -1  'True
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1695
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   19815
   End
End
Attribute VB_Name = "form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim yourMsg As Integer
Dim a, b As String
Private Sub Command1_Click()
Text2.PasswordChar = ""
End Sub
Private Sub Command2_Click()
Text2.PasswordChar = "*"
End Sub

Private Sub Form_Load()
Text2.PasswordChar = "*"
End Sub

Private Sub login_click()
a = "ips"
b = "1234"
If a = Text1.Text And b = Text2.Text Then
Form2.Show
form1.Hide
Else: yourMsg = MsgBox("incorrect username or password", vbRetryCancel + vbExclamation, "Error")
    If yourMsg = 2 Then
    End
    Else
    End If
End If
End Sub


