VERSION 5.00
Begin VB.Form Form18 
   BackColor       =   &H000000FF&
   ClientHeight    =   10935
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   BeginProperty Font 
      Name            =   "MS Sans Serif"
      Size            =   24
      Charset         =   0
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form1"
   ScaleHeight     =   1950
   ScaleMode       =   0  'User
   ScaleWidth      =   14050
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command5 
      Caption         =   "next"
      Height          =   1095
      Left            =   5760
      TabIndex        =   24
      Top             =   9120
      Width           =   2895
   End
   Begin VB.CommandButton Command3 
      Caption         =   "exit"
      Height          =   855
      Left            =   17400
      TabIndex        =   23
      Top             =   9600
      Width           =   2535
   End
   Begin VB.CommandButton Command2 
      Caption         =   "clear"
      Height          =   975
      Left            =   13560
      TabIndex        =   22
      Top             =   9480
      Width           =   3255
   End
   Begin VB.CommandButton Command1 
      Caption         =   "go"
      Height          =   855
      Left            =   11160
      TabIndex        =   21
      Top             =   9480
      Width           =   1215
   End
   Begin VB.TextBox Text6 
      BackColor       =   &H00FF0000&
      Height          =   1155
      Left            =   13080
      TabIndex        =   20
      Top             =   7440
      Width           =   6855
   End
   Begin VB.TextBox Text5 
      BackColor       =   &H00FF0000&
      Height          =   1215
      Left            =   13080
      TabIndex        =   18
      Top             =   5160
      Width           =   6855
   End
   Begin VB.TextBox Text4 
      BackColor       =   &H00FF0000&
      Height          =   1095
      Left            =   12960
      TabIndex        =   16
      Top             =   3360
      Width           =   6975
   End
   Begin VB.TextBox Text3 
      BackColor       =   &H00FF0000&
      Height          =   1095
      Left            =   12960
      TabIndex        =   14
      Top             =   1440
      Width           =   6975
   End
   Begin VB.TextBox Text2 
      BackColor       =   &H00FF0000&
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   930
      Left            =   6000
      TabIndex        =   9
      Top             =   1440
      Width           =   3975
   End
   Begin VB.TextBox Text1 
      BackColor       =   &H00FF0000&
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   915
      Left            =   1800
      TabIndex        =   6
      Top             =   1440
      Width           =   3255
   End
   Begin VB.CommandButton Command16 
      Caption         =   "/"
      Height          =   1035
      Left            =   8160
      TabIndex        =   5
      Top             =   3120
      Width           =   1215
   End
   Begin VB.CommandButton Command15 
      Caption         =   "divisibility rule"
      Height          =   1035
      Left            =   5160
      TabIndex        =   4
      Top             =   3120
      Width           =   2655
   End
   Begin VB.CommandButton Command14 
      Caption         =   "clear"
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   915
      Left            =   360
      TabIndex        =   3
      Top             =   9240
      Width           =   3015
   End
   Begin VB.CommandButton Command12 
      Caption         =   "-"
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1035
      Left            =   3720
      TabIndex        =   2
      Top             =   3120
      Width           =   1215
   End
   Begin VB.CommandButton Command8 
      Caption         =   "*"
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1035
      Left            =   2160
      TabIndex        =   1
      Top             =   3120
      Width           =   1215
   End
   Begin VB.CommandButton Command4 
      Caption         =   "+"
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1035
      Left            =   600
      TabIndex        =   0
      Top             =   3120
      Width           =   1215
   End
   Begin VB.Label Label9 
      BackStyle       =   0  'Transparent
      Caption         =   "monthly payment"
      Height          =   1215
      Left            =   10320
      TabIndex        =   19
      Top             =   7440
      Width           =   2895
   End
   Begin VB.Label Label8 
      BackStyle       =   0  'Transparent
      Caption         =   "monthly interest rate"
      Height          =   1335
      Left            =   10320
      TabIndex        =   17
      Top             =   5160
      Width           =   2775
   End
   Begin VB.Label Label7 
      BackStyle       =   0  'Transparent
      Caption         =   "no. of months"
      Height          =   1215
      Left            =   10560
      TabIndex        =   15
      Top             =   3360
      Width           =   2295
   End
   Begin VB.Line Line2 
      X1              =   7077.037
      X2              =   7077.037
      Y1              =   192.414
      Y2              =   577.064
   End
   Begin VB.Label Label6 
      BackStyle       =   0  'Transparent
      Caption         =   "amount borrowed"
      Height          =   1095
      Left            =   10560
      TabIndex        =   13
      Top             =   1440
      Width           =   2655
   End
   Begin VB.Label Label5 
      BackStyle       =   0  'Transparent
      Caption         =   "monthly loan payment"
      Height          =   615
      Left            =   12600
      TabIndex        =   12
      Top             =   240
      Width           =   6135
   End
   Begin VB.Label Label4 
      BackColor       =   &H000000FF&
      Caption         =   "calculator"
      Height          =   615
      Left            =   3840
      TabIndex        =   11
      Top             =   120
      Width           =   2535
   End
   Begin VB.Label Label3 
      BackColor       =   &H000080FF&
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   3855
      Left            =   240
      TabIndex        =   10
      Top             =   4680
      Width           =   9615
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "b="
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   975
      Left            =   5160
      TabIndex        =   8
      Top             =   1320
      Width           =   1455
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "A="
      BeginProperty Font 
         Name            =   "Arial"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   855
      Left            =   120
      TabIndex        =   7
      Top             =   1560
      Width           =   1455
   End
   Begin VB.Line Line1 
      BorderWidth     =   10
      X1              =   7077.037
      X2              =   6993.778
      Y1              =   21.399
      Y2              =   1966.049
   End
End
Attribute VB_Name = "Form18"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a, i, p, r, f, n As Currency

Private Sub Command1_Click()
p = Val(Text3.Text)
n = Val(Text4.Text)
i = Val(Text5.Text)
r = 0.01 * i / 12
f = (1 + r) ^ n
a = p * r * f / f - 1
Text6.Text = a
End Sub

Private Sub Command12_Click()
a = Val(Text1.Text)
i = Val(Text2.Text)
p = a - i
Label3.Caption = p
End Sub

Private Sub Command14_Click()
Label3.Caption = ""
End Sub

Private Sub Command15_Click()
a = Val(Text1.Text)
i = Val(Text2.Text)
If a Mod i = 0 Then
Label3.Caption = "it Is divisible"
Else: Label3.Caption = "it Is Not divisible"
End If
End Sub

Private Sub Command16_Click()
a = Val(Text1.Text)
i = Val(Text2.Text)
p = a / i
Label3.Caption = p
End Sub

Private Sub Command2_Click()
Text3.Text = ""
Text4.Text = ""
Text5.Text = ""
Text6.Text = ""
End Sub

Private Sub Command3_Click()
End
End Sub

Private Sub Command4_Click()
a = Val(Text1.Text)
i = Val(Text2.Text)
p = a + i
Label3.Caption = p
End Sub

Private Sub Command5_Click()
End
End Sub

Private Sub Command8_Click()
a = Val(Text1.Text)
i = Val(Text2.Text)
p = a * i
Label3.Caption = p
End Sub

