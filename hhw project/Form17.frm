VERSION 5.00
Begin VB.Form Form17 
   BackColor       =   &H000000FF&
   Caption         =   "Form17"
   ClientHeight    =   10950
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   20250
   BeginProperty Font 
      Name            =   "Matura MT Script Capitals"
      Size            =   48
      Charset         =   0
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form17"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   3  'Windows Default
   Begin VB.CommandButton Command5 
      BackColor       =   &H00FF0000&
      Caption         =   "credits"
      Height          =   1935
      Left            =   7440
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   8400
      Width           =   6375
   End
   Begin VB.CommandButton Command4 
      BackColor       =   &H00FF0000&
      Caption         =   "area of rombus and trapisium"
      Height          =   2055
      Left            =   11280
      Style           =   1  'Graphical
      TabIndex        =   4
      Top             =   5760
      Width           =   8775
   End
   Begin VB.CommandButton Command3 
      BackColor       =   &H00FF0000&
      Caption         =   "piggy bank and celcius to fahrenhiet  converter"
      Height          =   2175
      Left            =   0
      Style           =   1  'Graphical
      TabIndex        =   3
      Top             =   5640
      Width           =   9855
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00FF0000&
      Caption         =   "area of equilateral triangle and circle"
      Height          =   2175
      Left            =   11160
      Style           =   1  'Graphical
      TabIndex        =   2
      Top             =   2400
      Width           =   8895
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "Calculator and monthly loan payment"
      Height          =   2175
      Left            =   0
      Style           =   1  'Graphical
      TabIndex        =   1
      Top             =   2400
      Width           =   9735
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "Welcome to the Mega  Calculator 2019"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   54
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   -1  'True
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1575
      Left            =   360
      TabIndex        =   0
      Top             =   360
      Width           =   20175
   End
End
Attribute VB_Name = "Form17"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
Form18.Show
End Sub

Private Sub Command2_Click()
Form19.Show
End Sub

Private Sub Command3_Click()
Form20.Show
End Sub

Private Sub Command4_Click()
Form21.Show
End Sub

Private Sub Command5_Click()
Form23.Show
End Sub
