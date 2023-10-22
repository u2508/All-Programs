VERSION 5.00
Begin VB.Form Form19 
   BackColor       =   &H00FF0000&
   Caption         =   "Form3"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   LinkTopic       =   "Form3"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command5 
      Caption         =   "clear"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   54.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   15600
      TabIndex        =   14
      Top             =   8400
      Width           =   3855
   End
   Begin VB.CommandButton Command4 
      Caption         =   "go"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   54.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   12480
      TabIndex        =   13
      Top             =   8400
      Width           =   2775
   End
   Begin VB.CommandButton Command3 
      Caption         =   "exit"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   54.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   8280
      TabIndex        =   12
      Top             =   8400
      Width           =   3855
   End
   Begin VB.TextBox Text2 
      BackColor       =   &H000000FF&
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   13920
      TabIndex        =   9
      Top             =   3840
      Width           =   5415
   End
   Begin VB.CommandButton Command2 
      Caption         =   "clear"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1155
      Left            =   3960
      TabIndex        =   6
      Top             =   8400
      Width           =   3975
   End
   Begin VB.CommandButton Command1 
      Caption         =   "go"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1155
      Left            =   360
      TabIndex        =   5
      Top             =   8400
      Width           =   3255
   End
   Begin VB.TextBox Text1 
      BackColor       =   &H000000FF&
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1575
      Left            =   3600
      TabIndex        =   2
      Top             =   3840
      Width           =   6015
   End
   Begin VB.Label Label8 
      BackColor       =   &H000000FF&
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   14040
      TabIndex        =   11
      Top             =   5880
      Width           =   5295
   End
   Begin VB.Label Label7 
      BackStyle       =   0  'Transparent
      Caption         =   "area:-"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1335
      Left            =   9960
      TabIndex        =   10
      Top             =   5760
      Width           =   3975
   End
   Begin VB.Label Label6 
      BackStyle       =   0  'Transparent
      Caption         =   "radius"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   9840
      TabIndex        =   8
      Top             =   3840
      Width           =   3975
   End
   Begin VB.Label Label5 
      BackStyle       =   0  'Transparent
      Caption         =   "area of circle"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1575
      Left            =   10080
      TabIndex        =   7
      Top             =   480
      Width           =   8535
   End
   Begin VB.Label Label4 
      BackColor       =   &H000000FF&
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
      Left            =   3600
      TabIndex        =   4
      Top             =   5640
      Width           =   6015
   End
   Begin VB.Label Label3 
      BackStyle       =   0  'Transparent
      Caption         =   "area:-"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   0
      TabIndex        =   3
      Top             =   5520
      Width           =   3615
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "side:-"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   120
      TabIndex        =   1
      Top             =   3840
      Width           =   3615
   End
   Begin VB.Line Line1 
      BorderWidth     =   10
      X1              =   9600
      X2              =   9960
      Y1              =   0
      Y2              =   10920
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "area of equilateral triangle"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   54.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   2775
      Left            =   0
      TabIndex        =   0
      Top             =   240
      Width           =   9015
   End
End
Attribute VB_Name = "Form19"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a, r As Currency

Private Sub Command1_Click()
Label4.Caption = 1.732 * 0.25 * Text1.Text * Text1.Text
End Sub

Private Sub Command2_Click()
Text1.Text = ""
Label4.Caption = ""
End Sub

Private Sub Command3_Click()
End
End Sub

Private Sub Command4_Click()
Label8.Caption = 3.14 * Text2.Text * Text2.Text
End Sub

Private Sub Command5_Click()
Text2.Text = ""
Label8.Caption = ""
End Sub
