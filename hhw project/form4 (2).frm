VERSION 5.00
Begin VB.Form Form20 
   BackColor       =   &H000000FF&
   Caption         =   "Form2"
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
   LinkTopic       =   "Form2"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command5 
      Caption         =   "clear"
      Height          =   1080
      Left            =   4320
      TabIndex        =   21
      Top             =   9000
      Width           =   3135
   End
   Begin VB.CommandButton Command4 
      Caption         =   "clear"
      Height          =   1095
      Left            =   16440
      TabIndex        =   20
      Top             =   9000
      Width           =   3495
   End
   Begin VB.CommandButton Command3 
      Caption         =   "go"
      Height          =   1095
      Left            =   13080
      TabIndex        =   19
      Top             =   9000
      Width           =   2895
   End
   Begin VB.TextBox Text7 
      BackColor       =   &H00FF0000&
      Height          =   1815
      Left            =   14880
      TabIndex        =   16
      Top             =   3240
      Width           =   5295
   End
   Begin VB.CommandButton Command2 
      Caption         =   "exit"
      Height          =   1095
      Left            =   7680
      TabIndex        =   13
      Top             =   9000
      Width           =   5175
   End
   Begin VB.CommandButton Command1 
      Caption         =   "go"
      Height          =   960
      Left            =   360
      TabIndex        =   12
      Top             =   9000
      Width           =   3735
   End
   Begin VB.TextBox Text5 
      BackColor       =   &H00FF0000&
      Height          =   1080
      Left            =   4680
      TabIndex        =   7
      Top             =   5880
      Width           =   5415
   End
   Begin VB.TextBox Text4 
      BackColor       =   &H00FF0000&
      Height          =   1320
      Left            =   4680
      TabIndex        =   6
      Top             =   4560
      Width           =   5445
   End
   Begin VB.TextBox Text3 
      BackColor       =   &H00FF0000&
      Height          =   1215
      Left            =   4680
      TabIndex        =   5
      Top             =   3360
      Width           =   5415
   End
   Begin VB.TextBox Text2 
      BackColor       =   &H00FF0000&
      Height          =   1215
      Left            =   4680
      TabIndex        =   4
      Top             =   2160
      Width           =   5415
   End
   Begin VB.TextBox Text1 
      BackColor       =   &H00FF0000&
      Height          =   1050
      Left            =   4680
      TabIndex        =   2
      Top             =   1080
      Width           =   5415
   End
   Begin VB.Label Label12 
      BackColor       =   &H0000FF00&
      Height          =   1335
      Left            =   4560
      TabIndex        =   22
      Top             =   7440
      Width           =   5415
   End
   Begin VB.Label Label11 
      BackColor       =   &H0000FF00&
      Height          =   1695
      Left            =   14880
      TabIndex        =   18
      Top             =   6120
      Width           =   5295
   End
   Begin VB.Label Label10 
      BackStyle       =   0  'Transparent
      Caption         =   "temperature in fahrenhiet"
      Height          =   1695
      Left            =   10200
      TabIndex        =   17
      Top             =   6000
      Width           =   4695
   End
   Begin VB.Label Label9 
      BackStyle       =   0  'Transparent
      Caption         =   "temperature in cel"
      Height          =   1815
      Left            =   10200
      TabIndex        =   15
      Top             =   3240
      Width           =   4815
   End
   Begin VB.Label Label8 
      BackStyle       =   0  'Transparent
      Caption         =   "celcius to fahrenhiet temperature converter"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   2535
      Left            =   10200
      TabIndex        =   14
      Top             =   120
      Width           =   9975
   End
   Begin VB.Label Label7 
      BackStyle       =   0  'Transparent
      Caption         =   "TOTAL"
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
      Left            =   0
      TabIndex        =   11
      Top             =   7560
      Width           =   4455
   End
   Begin VB.Label Label6 
      BackStyle       =   0  'Transparent
      Caption         =   "five hundred rupees"
      Height          =   1815
      Left            =   120
      TabIndex        =   10
      Top             =   5520
      Width           =   4575
   End
   Begin VB.Label Label5 
      BackStyle       =   0  'Transparent
      Caption         =   "hundred rupees"
      Height          =   855
      Left            =   -120
      TabIndex        =   9
      Top             =   4680
      Width           =   4935
   End
   Begin VB.Label Label4 
      BackStyle       =   0  'Transparent
      Caption         =   "fifty rupees"
      Height          =   1095
      Left            =   120
      TabIndex        =   8
      Top             =   3480
      Width           =   4695
   End
   Begin VB.Label Label3 
      BackStyle       =   0  'Transparent
      Caption         =   "twenty rupees"
      Height          =   975
      Left            =   0
      TabIndex        =   3
      Top             =   2280
      Width           =   4575
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "ten rupees"
      Height          =   855
      Left            =   120
      TabIndex        =   1
      Top             =   1080
      Width           =   4455
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "piggy bank"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   48
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   2520
      TabIndex        =   0
      Top             =   -120
      Width           =   4935
   End
   Begin VB.Line Line1 
      BorderColor     =   &H00000000&
      BorderWidth     =   8
      X1              =   10080
      X2              =   10200
      Y1              =   0
      Y2              =   10440
   End
End
Attribute VB_Name = "Form20"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub Command1_Click()
Label12.Caption = 10 * Text1.Text + 20 * Text2.Text + 50 * Text3.Text + 100 * Text4.Text + 500 * Text5.Text
End Sub

Private Sub Command2_Click()
End
End Sub

Private Sub Command3_Click()
Label11.Caption = 9 / 5 * Text7.Text + 32
End Sub

Private Sub Command4_Click()
Label11.Caption = ""
End Sub

Private Sub Command5_Click()
Label12.Caption = ""
End Sub

