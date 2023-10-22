VERSION 5.00
Begin VB.Form Form15 
   BackColor       =   &H00FF0000&
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   LinkTopic       =   "Form14"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command4 
      BackColor       =   &H00FF0000&
      Caption         =   "credits"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   2895
      Left            =   13920
      Style           =   1  'Graphical
      TabIndex        =   3
      Top             =   4320
      Width           =   6255
   End
   Begin VB.CommandButton Command3 
      BackColor       =   &H00FF0000&
      Caption         =   "try our other app"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   120
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   2895
      Left            =   0
      Style           =   1  'Graphical
      TabIndex        =   2
      Top             =   7800
      Width           =   20295
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00FF0000&
      Caption         =   "exit the game"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   120
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   2895
      Left            =   0
      Style           =   1  'Graphical
      TabIndex        =   1
      Top             =   4320
      Width           =   13695
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "play again this game"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   114.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   3255
      Left            =   0
      Style           =   1  'Graphical
      TabIndex        =   0
      Top             =   480
      Width           =   20295
   End
End
Attribute VB_Name = "Form15"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
Form15.Hide
Form3.Show
End Sub
Private Sub Command2_Click()
End
End Sub

Private Sub Command3_Click()
Form15.Hide
Form2.Show
End Sub

Private Sub Command4_Click()
Form15.Hide
Form23.Show
End Sub
