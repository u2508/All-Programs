VERSION 5.00
Begin VB.Form Form14 
   BackColor       =   &H00FF0000&
   Caption         =   "bumper question round"
   ClientHeight    =   10950
   ClientLeft      =   225
   ClientTop       =   555
   ClientWidth     =   20250
   LinkTopic       =   "Form13"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command2 
      BackColor       =   &H00FF0000&
      Caption         =   "no, finish the quiz now"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   27.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1275
      Left            =   9240
      Style           =   1  'Graphical
      TabIndex        =   2
      Top             =   2880
      Width           =   5535
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00FF0000&
      Caption         =   "yes,play the bumper question"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   27.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1335
      Left            =   3360
      MaskColor       =   &H000000FF&
      Style           =   1  'Graphical
      TabIndex        =   1
      Top             =   2880
      UseMaskColor    =   -1  'True
      Width           =   5415
   End
   Begin VB.Frame Frame1 
      BackColor       =   &H000000FF&
      Height          =   6520
      Left            =   2280
      TabIndex        =   0
      Top             =   4320
      Width           =   12570
      Begin VB.CommandButton Command4 
         BackColor       =   &H000000FF&
         Caption         =   "finish the quiz"
         BeginProperty Font 
            Name            =   "MS Reference Sans Serif"
            Size            =   36
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   975
         Left            =   5280
         Style           =   1  'Graphical
         TabIndex        =   7
         Top             =   5160
         Width           =   6975
      End
      Begin VB.CommandButton Command3 
         BackColor       =   &H000000FF&
         Caption         =   "check answer"
         BeginProperty Font 
            Name            =   "MS Reference Sans Serif"
            Size            =   27.75
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   975
         Left            =   360
         Style           =   1  'Graphical
         TabIndex        =   6
         Top             =   5160
         Width           =   4335
      End
      Begin VB.TextBox Text1 
         BackColor       =   &H0000FF00&
         Height          =   2655
         Left            =   1200
         TabIndex        =   5
         Top             =   1920
         Width           =   10575
      End
      Begin VB.Label Label3 
         BackStyle       =   0  'Transparent
         Caption         =   "Q 11 . What came first a hen or an egg ? give reason."
         BeginProperty Font 
            Name            =   "MS Reference Sans Serif"
            Size            =   27.75
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   1455
         Left            =   120
         TabIndex        =   4
         Top             =   360
         Width           =   12135
      End
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   " do you  want to play  the bumper question ?"
      BeginProperty Font 
         Name            =   "MS Reference Sans Serif"
         Size            =   36
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   2055
      Left            =   3360
      TabIndex        =   3
      Top             =   480
      Width           =   11415
   End
End
Attribute VB_Name = "Form14"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False


Private Sub Command1_Click()
Frame1.Visible = True
End Sub

Private Sub Command2_Click()
Form14.Hide
Form15.Show
End Sub

Private Sub Command3_Click()
Dim a As String
a = "Basically, many, many moons ago there was a chicken-like bird. It was genetically close to a chicken but wasn't a full-blown chicken yet. The video calls it a proto-chicken. So proto-hen laid an egg, and proto-rooster fertilized it. But when the genes from ma and pa almost-chicken fused, they combined in a new way, creating a mutation that accidentally made the baby different from its parents. Although it would take millennia for the difference to be noticed, that egg was different enough to become the official progenitor of a new species, now known as the chicken! So in a nutshell (or an eggshell, if you like), two birds that weren't really chickens created a chicken egg, and hence, we have an answer: The egg came first, and then it hatched a chicken."
If b = Text1.Text Then
MsgBox "your answer is correct"
Else: MsgBox "your answer is wrong"
End If
End Sub

Private Sub Command4_Click()
Form14.Hide
Form15.Show
End Sub

Private Sub Form_Load()
Frame1.Visible = False
End Sub

