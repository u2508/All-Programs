VERSION 5.00
Begin VB.Form Form23 
   BackColor       =   &H000000FF&
   Caption         =   "Form22"
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
   LinkTopic       =   "Form6"
   ScaleHeight     =   10950
   ScaleWidth      =   20250
   StartUpPosition =   2  'CenterScreen
   Begin VB.CommandButton Command1 
      BackColor       =   &H000000FF&
      Caption         =   "Exit"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1275
      Left            =   7680
      Style           =   1  'Graphical
      TabIndex        =   8
      Top             =   9240
      Width           =   5655
   End
   Begin VB.Frame Frame2 
      BackColor       =   &H000000FF&
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   1.5
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   5415
      Left            =   11400
      TabIndex        =   4
      Top             =   3480
      Width           =   7935
      Begin VB.Label Label6 
         BackStyle       =   0  'Transparent
         Caption         =   "kbcliv.in"
         Height          =   1215
         Left            =   2040
         TabIndex        =   7
         Top             =   3720
         Width           =   7935
      End
      Begin VB.Line Line1 
         BorderWidth     =   4
         X1              =   0
         X2              =   7920
         Y1              =   2760
         Y2              =   2760
      End
      Begin VB.Label Label5 
         BackStyle       =   0  'Transparent
         Caption         =   "Source"
         Height          =   1215
         Left            =   2160
         TabIndex        =   6
         Top             =   2640
         Width           =   3855
      End
      Begin VB.Label Label4 
         BackStyle       =   0  'Transparent
         Caption         =   "This app was made using VB"
         Height          =   2415
         Left            =   360
         TabIndex        =   5
         Top             =   360
         Width           =   7455
      End
   End
   Begin VB.Frame Frame1 
      BackColor       =   &H000000FF&
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   1.5
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   5415
      Left            =   1200
      TabIndex        =   2
      Top             =   3480
      Width           =   8895
      Begin VB.Label Label3 
         BackStyle       =   0  'Transparent
         Caption         =   " Special thanks to Mr Utkarsh Gupta    Founder Ceo       Omega Producers"
         Height          =   5175
         Left            =   120
         TabIndex        =   3
         Top             =   120
         Width           =   8895
      End
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "Credits"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   72
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1815
      Left            =   7560
      TabIndex        =   1
      Top             =   1560
      Width           =   4935
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "Thanks for using this application"
      BeginProperty Font 
         Name            =   "Matura MT Script Capitals"
         Size            =   66
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1815
      Left            =   120
      TabIndex        =   0
      Top             =   240
      Width           =   20055
   End
End
Attribute VB_Name = "Form23"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
End
End Sub
