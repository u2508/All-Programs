VERSION 5.00
Begin VB.Form Form21 
   BackColor       =   &H00FF0000&
   Caption         =   "Form5"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   BeginProperty Font 
      Name            =   "Matura MT Script Capitals"
      Size            =   36
      Charset         =   0
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form5"
   ScaleHeight     =   10950
   ScaleMode       =   0  'User
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command5 
      Caption         =   "clear"
      Height          =   1095
      Left            =   16680
      TabIndex        =   20
      Top             =   9600
      Width           =   3375
   End
   Begin VB.CommandButton Command4 
      Caption         =   "find area"
      Height          =   1095
      Left            =   12480
      TabIndex        =   19
      Top             =   9600
      Width           =   3975
   End
   Begin VB.TextBox Text6 
      BackColor       =   &H000000FF&
      Height          =   1335
      Left            =   15960
      TabIndex        =   13
      Top             =   6000
      Width           =   4095
   End
   Begin VB.TextBox Text5 
      BackColor       =   &H000000FF&
      Height          =   1695
      Left            =   15960
      TabIndex        =   12
      Top             =   4080
      Width           =   4095
   End
   Begin VB.TextBox Text4 
      BackColor       =   &H000000FF&
      Height          =   1815
      Left            =   15960
      TabIndex        =   11
      Top             =   2160
      Width           =   4095
   End
   Begin VB.CommandButton Command3 
      Caption         =   "clear"
      Height          =   1095
      Left            =   240
      TabIndex        =   9
      Top             =   9480
      Width           =   3855
   End
   Begin VB.CommandButton Command2 
      Caption         =   "exit"
      Height          =   1095
      Left            =   8400
      TabIndex        =   8
      Top             =   9600
      Width           =   3855
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FFFFFF&
      Caption         =   "find area"
      Height          =   1095
      Left            =   4440
      Style           =   1  'Graphical
      TabIndex        =   7
      Top             =   9600
      Width           =   3615
   End
   Begin VB.TextBox Text2 
      BackColor       =   &H000000FF&
      Height          =   1695
      Left            =   6000
      TabIndex        =   5
      Top             =   5160
      Width           =   3975
   End
   Begin VB.TextBox Text1 
      BackColor       =   &H000000FF&
      Height          =   1575
      Left            =   6120
      TabIndex        =   3
      Top             =   2160
      Width           =   3855
   End
   Begin VB.Label Label11 
      BackColor       =   &H000000FF&
      Height          =   1455
      Left            =   14040
      TabIndex        =   18
      Top             =   7560
      Width           =   6135
   End
   Begin VB.Label Label10 
      BackColor       =   &H000000FF&
      Height          =   1695
      Left            =   3480
      TabIndex        =   17
      Top             =   7560
      Width           =   6495
   End
   Begin VB.Label Label9 
      BackStyle       =   0  'Transparent
      Caption         =   "AREA"
      Height          =   1455
      Left            =   10440
      TabIndex        =   16
      Top             =   7800
      Width           =   5175
   End
   Begin VB.Label Label8 
      BackStyle       =   0  'Transparent
      Caption         =   "height "
      Height          =   975
      Left            =   10440
      TabIndex        =   15
      Top             =   6240
      Width           =   4935
   End
   Begin VB.Label Label7 
      BackStyle       =   0  'Transparent
      Caption         =   "lenght of parallel side 2"
      Height          =   1695
      Left            =   10320
      TabIndex        =   14
      Top             =   4080
      Width           =   5535
   End
   Begin VB.Label Label6 
      BackStyle       =   0  'Transparent
      Caption         =   "lenght of parallel side 1"
      Height          =   1695
      Left            =   10320
      TabIndex        =   10
      Top             =   2040
      Width           =   5655
   End
   Begin VB.Label Label5 
      BackStyle       =   0  'Transparent
      Caption         =   "AREA"
      Height          =   1695
      Left            =   120
      TabIndex        =   6
      Top             =   7800
      Width           =   4575
   End
   Begin VB.Label Label4 
      BackStyle       =   0  'Transparent
      Caption         =   "lenght of diagonal 2"
      Height          =   1815
      Left            =   120
      TabIndex        =   4
      Top             =   5040
      Width           =   5895
   End
   Begin VB.Label Label3 
      BackStyle       =   0  'Transparent
      Caption         =   "lenght of diagonal 1"
      Height          =   1695
      Left            =   240
      TabIndex        =   2
      Top             =   2040
      Width           =   6015
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "area of trapisium"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   65.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1455
      Left            =   10320
      TabIndex        =   1
      Top             =   240
      Width           =   9855
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "area of rombus "
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
      TabIndex        =   0
      Top             =   120
      Width           =   9465
   End
   Begin VB.Line Line1 
      BorderWidth     =   10
      X1              =   10200
      X2              =   10080
      Y1              =   10920
      Y2              =   0
   End
End
Attribute VB_Name = "Form21"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub Command1_Click()
Label10.Caption = Text1.Text * Text2.Text
End Sub

Private Sub Command2_Click()
End
End Sub

Private Sub Command3_Click()
Text1.Text = ""
Text2.Text = ""
Label10.Caption = ""
End Sub

Private Sub Command4_Click()
Dim a, b, c, d, e As Integer
a = Val(Text4.Text)
b = Val(Text5.Text)
c = Val(Text6.Text)
If a <> 0 Then
    If b <> 0 Then
        If c <> 0 Then
        d = a + b
        e = d / 2
        Label11.Caption = e * c
        Else: Label11.Caption = "0"
        End If
    Else: Label11.Caption = "0"
    End If
Else: Label11.Caption = "0"
End If
End Sub

Private Sub Command5_Click()
Text4.Text = ""
Text5.Text = ""
Text6.Text = ""
Label11.Caption = ""
End Sub
