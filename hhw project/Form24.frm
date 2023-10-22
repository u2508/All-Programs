VERSION 5.00
Begin VB.Form Form24 
   BackColor       =   &H0000FF00&
   Caption         =   "Form24"
   ClientHeight    =   9090
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   16800
   BeginProperty Font 
      Name            =   "Matura MT Script Capitals"
      Size            =   48
      Charset         =   0
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form24"
   ScaleHeight     =   9090
   ScaleWidth      =   16800
   StartUpPosition =   3  'Windows Default
   Begin VB.CommandButton Command1 
      BackColor       =   &H0000FF00&
      Caption         =   "add entry"
      DragMode        =   1  'Automatic
      Height          =   1275
      Left            =   5520
      Style           =   1  'Graphical
      TabIndex        =   4
      Top             =   3600
      Width           =   5055
   End
   Begin VB.ListBox List1 
      BackColor       =   &H0000FF00&
      ForeColor       =   &H000000FF&
      Height          =   2670
      ItemData        =   "Form24.frx":0000
      Left            =   2760
      List            =   "Form24.frx":0002
      Style           =   1  'Checkbox
      TabIndex        =   3
      Top             =   5160
      Width           =   9255
   End
   Begin VB.TextBox Text1 
      BackColor       =   &H0000FF00&
      Height          =   1395
      Left            =   6480
      TabIndex        =   2
      Top             =   1920
      Width           =   5535
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "book name"
      Height          =   1335
      Left            =   1200
      TabIndex        =   1
      Top             =   2040
      Width           =   5055
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "book depot"
      Height          =   1335
      Left            =   5880
      TabIndex        =   0
      Top             =   240
      Width           =   4575
   End
End
Attribute VB_Name = "Form24"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub Command1_Click()
 List1.List = Text1.Text
End Sub
