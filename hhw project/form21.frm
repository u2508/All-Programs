VERSION 5.00
Begin VB.Form Form3 
   BackColor       =   &H00FF0000&
   Caption         =   "personal details"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   LinkTopic       =   "Form2"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "lets play"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   36
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   2880
      MaskColor       =   &H00FF0000&
      Style           =   1  'Graphical
      TabIndex        =   7
      Top             =   9120
      UseMaskColor    =   -1  'True
      Width           =   6135
   End
   Begin VB.Frame Frame1 
      BackColor       =   &H00FF0000&
      Height          =   8895
      Left            =   600
      TabIndex        =   0
      Top             =   1920
      Width           =   19455
      Begin VB.Frame Frame2 
         BackColor       =   &H00FF0000&
         ForeColor       =   &H8000000F&
         Height          =   5655
         Left            =   480
         TabIndex        =   5
         Top             =   3000
         Width           =   16215
         Begin VB.Timer Timer1 
            Left            =   3480
            Top             =   2520
         End
         Begin VB.CommandButton Command2 
            BackColor       =   &H00FF0000&
            Caption         =   "exit the game"
            BeginProperty Font 
               Name            =   "MS Reference Sans Serif"
               Size            =   36
               Charset         =   0
               Weight          =   700
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            Height          =   1095
            Left            =   8760
            Style           =   1  'Graphical
            TabIndex        =   9
            Top             =   4200
            Width           =   6735
         End
         Begin VB.Label Label6 
            BackStyle       =   0  'Transparent
            Caption         =   "10"
            BeginProperty Font 
               Name            =   "MS Reference Sans Serif"
               Size            =   72
               Charset         =   0
               Weight          =   700
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            Height          =   1815
            Left            =   8400
            TabIndex        =   8
            Top             =   2160
            Width           =   2295
         End
         Begin VB.Label Label5 
            BackColor       =   &H00FF0000&
            BackStyle       =   0  'Transparent
            Caption         =   "  game  starting  in"
            BeginProperty Font 
               Name            =   "MS Reference Sans Serif"
               Size            =   72
               Charset         =   0
               Weight          =   700
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            Height          =   2175
            Left            =   360
            TabIndex        =   6
            Top             =   360
            Width           =   15135
         End
      End
      Begin VB.Label Label4 
         BackColor       =   &H00FF0000&
         BackStyle       =   0  'Transparent
         Caption         =   "gmail:-utkarshgupta64825@gmail.com"
         DragMode        =   1  'Automatic
         BeginProperty Font 
            Name            =   "MS Reference Sans Serif"
            Size            =   30
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H00000000&
         Height          =   975
         Left            =   240
         TabIndex        =   4
         Top             =   1680
         Width           =   12615
      End
      Begin VB.Label Label3 
         BackColor       =   &H00FF0000&
         Caption         =   "phone :- 8368567872 "
         BeginProperty Font 
            Name            =   "MS Reference Sans Serif"
            Size            =   30
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   975
         Left            =   8280
         TabIndex        =   3
         Top             =   360
         Width           =   6975
      End
      Begin VB.Label Label2 
         BackColor       =   &H00FF0000&
         Caption         =   "name:-Utkarsh Gupta"
         BeginProperty Font 
            Name            =   "MS Reference Sans Serif"
            Size            =   30
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   975
         Left            =   240
         TabIndex        =   2
         Top             =   360
         Width           =   8295
      End
   End
   Begin VB.Label Label1 
      BackColor       =   &H00FF0000&
      BackStyle       =   0  'Transparent
      BorderStyle     =   1  'Fixed Single
      Caption         =   "kaun banega karodpati"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   48
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1215
      Left            =   3480
      TabIndex        =   1
      Top             =   240
      Width           =   11415
   End
End
Attribute VB_Name = "Form3"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim a As Double
Private Sub Command1_Click()
Form4.Show
Form3.Hide
End Sub

Private Sub Command2_Click()
End
End Sub

Private Sub Form_Load()
Timer1.Enabled = True
Timer1.Interval = 1000
a = 10
End Sub

Private Sub Timer1_Timer()
a = a - 1
Me.Label6.Caption = a
If a = 0 Then
Timer1.Enabled = False
MsgBox "click on lets play to play or click on exit the game to exit"
End If
End Sub
