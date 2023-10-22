VERSION 5.00
Begin VB.Form Form2 
   BackColor       =   &H000000FF&
   Caption         =   "application selection"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   LinkTopic       =   "Form16"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command1 
      Caption         =   "Command1"
      Height          =   375
      Left            =   4560
      TabIndex        =   5
      Top             =   240
      Width           =   1575
   End
   Begin VB.OptionButton Option1 
      BackColor       =   &H00FF0000&
      Caption         =   "Option1"
      Height          =   950
      Left            =   240
      TabIndex        =   4
      Top             =   6360
      Value           =   -1  'True
      Width           =   195
   End
   Begin VB.OptionButton Option4 
      BackColor       =   &H00FF0000&
      Caption         =   "Class 11 Fee Structure calculator"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   60
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   -1  'True
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1515
      Left            =   240
      TabIndex        =   3
      Top             =   8880
      Width           =   19815
   End
   Begin VB.OptionButton Option3 
      BackColor       =   &H00FF0000&
      Caption         =   "MEGA CALCULATOR 2019"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   50.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   2175
      Left            =   240
      TabIndex        =   2
      Top             =   5760
      Width           =   19695
   End
   Begin VB.OptionButton Option2 
      BackColor       =   &H00FF0000&
      Caption         =   "KAUN BANEGA KARODPATI"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   42
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   2295
      Left            =   240
      TabIndex        =   1
      Top             =   2400
      Width           =   19815
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "which app do you want to open"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   -1  'True
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00FF0000&
      Height          =   2175
      Left            =   240
      TabIndex        =   0
      Top             =   480
      Width           =   19575
   End
End
Attribute VB_Name = "Form2"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
Form24.Show
End Sub

Private Sub Option2_Click()
If Option2 = True Then
Form3.Show
End If
End Sub

Private Sub Option3_Click()
If Option3 = True Then
Form17.Show
End If
End Sub

Private Sub Option4_Click()
If Option4 = True Then
Form22.Show
End If
End Sub
