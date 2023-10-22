VERSION 5.00
Begin VB.Form Form16 
   BackColor       =   &H00FF0000&
   Caption         =   "Form15"
   ClientHeight    =   10950
   ClientLeft      =   -150
   ClientTop       =   555
   ClientWidth     =   20250
   LinkTopic       =   "Form15"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "sorry you have given wrong answer. try again."
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   60
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   10935
      Left            =   15480
      Style           =   1  'Graphical
      TabIndex        =   0
      Top             =   0
      Width           =   4695
   End
   Begin VB.Image Image1 
      Height          =   10800
      Left            =   0
      Picture         =   "Form15.frx":0000
      Top             =   0
      Width           =   19200
   End
End
Attribute VB_Name = "Form16"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
Form15.Hide
Form2.Show
End Sub

Private Sub Image1_Click()

End Sub
