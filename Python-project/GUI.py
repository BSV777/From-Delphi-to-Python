#!/usr/bin/env python
# -*- coding: utf-8 -*-

# var
#   MainForm: TMainForm
#   Panel: TPanel
#   CurrentPanel, Count, CurrentShape:integer
#   PanelList:TList
#
# const
#   X0:integer=0
#   Y0:integer=0
#   Xk:integer=0
#   Yk:integer=0
#   L0:integer=0
#   T0:integer=0
#   W0:integer=0
#   H0:integer=0
#   Lk:integer=0
#   Tk:integer=0
#   Wk:integer=0
#   Hk:integer=0
#   Modified:boolean=False
#   DefaultFileName:string='Untitled'
#   CurrentFileName:string='Untitled'
#   NeedCreate:integer=0
#   Valid:boolean=True
#
#
# mnAboutClick(Sender: TObject)
# AboutBox = nil
#      try
#      AboutBox = TAboutBox.Create(Self)
#      AboutBox.ShowModal
#      finally
#      if Assigned(AboutBox): AboutBox.Release
#
# FormCreate(Sender: TObject)
# var i:integer
# Application.ShowHint = True
# mnCrBtn.OnClick = sbCrBtnClick
# mnCrTxt.OnClick = sbCrTxtClick
# mnCrLab.OnClick = sbCrLabClick
# mnDel.OnClick = pmDelClick
# for i = 0 to MainForm.ComponentCount-1: if MainForm.Components[i] is TShape:
#      with TShape(MainForm.Components[i]):
#      OnMouseDown = PanelMouseDown
#      OnMouseMove = ShapeMouseMove
# SgProp.ColWidths[0] = 40
# SgProp.Cells[0, 0] = 'Left'
# SgProp.ColWidths[1] = 40
# SgProp.Cells[1, 0] = 'Top'
# SgProp.ColWidths[2] = 40
# SgProp.Cells[2, 0] = 'Width'
# SgProp.ColWidths[3] = 40
# SgProp.Cells[3, 0] = 'Height'
# SgProp.ColWidths[4] = 129
# SgProp.Cells[4, 0] = 'Caption'
# PanelList = TList.Create
# MnNewClick(Sender)
#
#
# FormResize(Sender: TObject)
# SbDesk.Width = Width-11
# SbDesk.Height = Height-89
# SgProp.Width = Width-164
# SgProp.ColWidths[4] = Width-333
#
#
# PanelMouseMove(Sender: TObject Shift: TShiftState X, Y: Integer)
# var i,T1,L1:integer
# if (ssLeft in Shift) and ((X != X0) or (Y != Y0)):
#      SbDeskClick(Sender)
#      CurrentPanel = (Sender as TPanel).Tag
#      Panel = PanelList.Items[CurrentPanel]
#      with Panel:
#           T1 = Top
#           L1 = Left
#           Tk = Top + Y-Y0
#           Lk = Left + X-X0
#      with sbDesk:
#           if Tk<-VertScrollBar.Position: Tk = -VertScrollBar.Position + 1
#           if Lk<-HorzScrollBar.Position: Lk = -HorzScrollBar.Position + 1
#           if Tk + Hk + VertScrollBar.Position>VertScrollBar.Range: Tk = VertScrollBar.Range-Hk-VertScrollBar.Position-1
#           if Lk + Wk + HorzScrollBar.Position>HorzScrollBar.Range: Lk = HorzScrollBar.Range-Wk-HorzScrollBar.Position-1
#      i = 0
#      Valid = True
#           repeat
#           if MainForm.Components[i] is TPanel: with TPanel(MainForm.Components[i]):
#           if (i != CurrentPanel) and (Tk + Hk>Top) and (Tk<Top + Height) and (Lk + Wk>Left) and (Lk<Left + Width)then Valid = False
#           i = i + 1
#           until (Valid=False)or(i=MainForm.ComponentCount)
#      if not Valid:
#           Count = PanelList.Count-1
#           for i = 0 to Count:
#                if i != CurrentPanel:
#                     Panel = PanelList.Items[i]
#                     with Panel:
#                          if (T1>Top) and (L1<Left + Width) and (L1 + Wk>Left) and (Tk<Top + Height): Tk = Top + Height
#                          if (T1<Top) and (L1<Left + Width) and (L1 + Wk>Left) and (Tk + Hk>Top): Tk = Top-Hk
#                          if (L1>Left) and (T1 + Hk>Top) and (T1<Top + Height) and (Lk<Left + Width): Lk = Left + Width
#                          if (L1<Left) and (T1 + Hk>Top) and (T1<Top + Height) and (Lk + Wk>Left): Lk = Left-Wk
#
#           Refresh(Sender)
#
#
# PanelMouseDown(Sender: TObject Button: TMouseButton Shift: TShiftState X, Y: Integer)
# X0 = X
# Y0 = Y
# if Sender is TPanel: CurrentPanel = (Sender as TPanel).Tag
# Panel = PanelList.Items[CurrentPanel]
# with Panel:
#      L0 = Left
#      T0 = Top
#      H0 = Height
#      W0 = Width
#      Lk = Left
#      Tk = Top
#      Hk = Height
#      Wk = Width
#      if BevelOuter != bvLowered:
#           STopCenter.Visible = True
#           SBottomCenter.Visible = True
#            else
#           STopCenter.Visible = False
#           SBottomCenter.Visible = False
#      if BevelOuter=bvRaised: pmBtn.Enabled = False else pmBtn.Enabled = True
#      if BevelOuter=bvLowered: pmTxt.Enabled = False else pmTxt.Enabled = True
#      if BevelOuter=bvNone: pmLab.Enabled = False else pmLab.Enabled = True
# STopLeft.Visible = True
# SMiddleLeft.Visible = True
# SBottomLeft.Visible = True
# STopRight.Visible = True
# SMiddleRight.Visible = True
# SBottomRight.Visible = True
# mnDel.Enabled = True
# mnDel.ShortCut =  ShortCut(VK_DELETE, [])
# Refresh(Sender)
#
#
# ShapeMouseMove(Sender: TObject Shift: TShiftState X, Y: Integer)
# var
#   i,T1,L1,H1,W1,VX,VY,CurrentShape:integer
# if ssLeft in Shift:
#      VX = X-X0
#      VY = Y-Y0
#      CurrentShape = (Sender as TShape).Tag
#      Panel = PanelList.Items[CurrentPanel]
#      T1 = Panel.Top
#      L1 = Panel.Left
#      H1 = Panel.Height
#      W1 = Panel.Width
#      if Panel.BevelOuter=bvLowered: VY = 0
#      case CurrentShape of
#      11:
#           Yk = STopLeft.Top + VY
#           Xk = STopLeft.Left + VX
#           Tk = Yk + 3
#           if Tk< -SbDesk.VertScrollBar.Position: Tk = -SbDesk.VertScrollBar.Position
#           Lk = Xk + 3
#           if Lk<-SbDesk.HorzScrollBar.Position: Lk = -SbDesk.HorzScrollBar.Position
#           Count = PanelList.Count-1
#           for i = 0 to Count:
#                if i != CurrentPanel:
#                     Panel = PanelList.Items[i]
#                     with Panel:
#                          if (T1>Top) and (L1<Left + Width) and (L1 + Wk>Left) and (Tk<Top + Height)then Tk = Top + Height
#                          if (L1>Left) and (T1 + Hk>Top) and (T1<Top + Height) and (Lk<Left + Width): Lk = Left + Width
#
#           Hk = H0 + T0-Tk
#           Wk = W0 + L0-Lk
#           if Wk < MinWidth:
#                Lk = L0 + W0-MinWidth
#                Wk = MinWidth
#           if Hk < MinHeight:
#                Tk = T0 + H0-MinHeight
#                Hk = MinHeight
#      12:
#           Yk = STopCenter.Top + VY
#           Tk = Yk + 3
#           if Tk< -SbDesk.VertScrollBar.Position: Tk = -SbDesk.VertScrollBar.Position
#           Count = PanelList.Count-1
#           for i = 0 to Count:
#                if i != CurrentPanel:
#                     Panel = PanelList.Items[i]
#                     with Panel: if (T1>Top) and (Lk<Left + Width) and (Lk + Wk>Left) and (Tk<Top + Height)then Tk = Top + Height
#
#           Hk = T0 + H0-Tk
#           if Hk < MinHeight:
#                Tk = T0 + H0-MinHeight
#                Hk = MinHeight
#      13:
#           Yk = STopRight.Top + VY
#           Xk = STopRight.Left + VX
#           Tk = Yk + 3
#           if Tk< -SbDesk.VertScrollBar.Position: Tk = -SbDesk.VertScrollBar.Position
#           if Lk + Wk + SbDesk.HorzScrollBar.Position > SbDesk.HorzScrollBar.Range:
#                Wk = SbDesk.HorzScrollBar.Range-Lk-SbDesk.HorzScrollBar.Position
#           Wk = Xk-L0 + 2
#           Count = PanelList.Count-1
#           for i = 0 to Count:
#                if i != CurrentPanel:
#                     Panel = PanelList.Items[i]
#                     with Panel:
#                          if (Lk<Left) and (T1 + Hk>Top) and (T1<Top + Height) and (Lk + Wk>Left): Wk = Left-Lk
#                          if (T1>Top) and (Lk<Left + Width) and (Lk + Wk>Left) and (Tk<Top + Height): Tk = Top + Height
#
#           Hk = H0 + T0-Tk
#           if Wk < MinWidth: Wk = MinWidth
#           if Hk < MinHeight:
#                Tk = T0 + H0-MinHeight
#                Hk = MinHeight
#      21:
#           Xk = SMiddleLeft.Left + VX
#           Lk = Xk + 3
#           if Lk<-SbDesk.HorzScrollBar.Position: Lk = -SbDesk.HorzScrollBar.Position
#           Count = PanelList.Count-1
#           for i = 0 to Count:
#                if i != CurrentPanel:
#                     Panel = PanelList.Items[i]
#                     with Panel: if (L1>Left) and (Tk + Hk>Top) and (Tk<Top + Height) and (Lk<Left + Width): Lk = Left + Width
#
#           Wk = W0 + L0-Lk
#           if Wk < MinWidth:
#                Lk = L0 + W0-MinWidth
#                Wk = MinWidth
#      23:
#           Xk = SMiddleRight.Left + VX
#           Wk = Xk-L0 + 2
#           Count = PanelList.Count-1
#           for i = 0 to Count:
#                if i != CurrentPanel:
#                     Panel = PanelList.Items[i]
#                     with Panel: if (Lk<Left) and (Tk + Hk>Top) and (Tk<Top + Height) and (Lk + Wk>Left): Wk = Left-Lk
#
#           if Lk + Wk + SbDesk.HorzScrollBar.Position > SbDesk.HorzScrollBar.Range:
#                Wk = SbDesk.HorzScrollBar.Range-Lk-SbDesk.HorzScrollBar.Position
#           if Wk < MinWidth: Wk = MinWidth
#
#      31:
#           Yk = SBottomLeft.Top + VY
#           Xk = SBottomLeft.Left + VX
#           Lk = Xk + 3
#           if Lk<-SbDesk.HorzScrollBar.Position: Lk = -SbDesk.HorzScrollBar.Position
#           Hk = Yk-T0 + 2
#           if Hk < MinHeight: Hk = MinHeight
#           if Tk + Hk + SbDesk.VertScrollBar.Position > SbDesk.VertScrollBar.Range:
#                Hk = SbDesk.VertScrollBar.Range-Tk-SbDesk.VertScrollBar.Position
#           Count = PanelList.Count-1
#           for i = 0 to Count:
#                if i != CurrentPanel:
#                     Panel = PanelList.Items[i]
#                     with Panel:
#                          if (Tk<Top) and (L1<Left + Width) and (L1 + Wk>Left) and (Tk + Hk>Top): Hk = Top-Tk
#                          if (L1>Left) and (Tk + Hk>Top) and (Tk<Top + Height) and (Lk<Left + Width): Lk = Left + Width
#
#           Wk = W0 + L0-Lk
#           if Wk < MinWidth:
#                Lk = L0 + W0-MinWidth
#                Wk = MinWidth
#      32:
#           Yk = SBottomCenter.Top + VY
#           Hk = Yk-T0 + 2
#           if Tk + Hk + SbDesk.VertScrollBar.Position > SbDesk.VertScrollBar.Range:
#                Hk = SbDesk.VertScrollBar.Range-Tk-SbDesk.VertScrollBar.Position
#           Count = PanelList.Count-1
#           for i = 0 to Count:
#                if i != CurrentPanel:
#                     Panel = PanelList.Items[i]
#                     with Panel: if (Tk<Top) and (Lk<Left + Width) and (Lk + Wk>Left) and (Tk + Hk>Top): Hk = Top-Tk
#
#           if Hk < MinHeight: Hk = MinHeight
#      33:
#           Yk = SBottomRight.Top + VY
#           Xk = SBottomRight.Left + VX
#           Hk = Yk-T0 + 2
#           if Hk < MinHeight: Hk = MinHeight
#           if Tk + Hk + SbDesk.VertScrollBar.Position > SbDesk.VertScrollBar.Range:
#                Hk = SbDesk.VertScrollBar.Range-Tk-SbDesk.VertScrollBar.Position
#           Wk = Xk-L0 + 2
#           if Wk < MinWidth: Wk = MinWidth
#           if Lk + Wk + SbDesk.HorzScrollBar.Position > SbDesk.HorzScrollBar.Range:
#                Wk = SbDesk.HorzScrollBar.Range-Lk-SbDesk.HorzScrollBar.Position
#           Count = PanelList.Count-1
#           for i = 0 to Count:
#                if i != CurrentPanel:
#                     Panel = PanelList.Items[i]
#                     with Panel:
#                          if (Lk<Left) and (Tk + H1>Top) and (Tk<Top + Height) and (Lk + Wk>Left): Wk = Left-Lk
#                          if (Tk<Top) and (Lk<Left + Width) and (Lk + W1>Left) and (Tk + Hk>Top): Hk = Top-Tk
#
#      Refresh(Sender)
#
#
# pmBtnClick(Sender: TObject)
# Panel = PanelList.Items[CurrentPanel]
# Panel.BevelOuter = bvRaised
# Panel.Color = clBtnFace
# Panel.Alignment = taCenter
# SgProp.Cells[4, 0] = 'Caption'
# STopCenter.Visible = True
# SBottomCenter.Visible = True
# Refresh(Sender)
#
#
# pmTxtClick(Sender: TObject)
# Panel = PanelList.Items[CurrentPanel]
# Panel.BevelOuter = bvLowered
# Panel.Color = clHighlightText
# Panel.Alignment = taLeftJustify
# Hk = MinHeight
# SgProp.Cells[4, 0] = 'Text'
# STopCenter.Visible = False
# SBottomCenter.Visible = False
# Refresh(Sender)
#
#
# pmLabClick(Sender: TObject)
# Panel = PanelList.Items[CurrentPanel]
# Panel.BevelOuter = bvNone
# Panel.Color = clBtnFace
# Panel.Alignment = taLeftJustify
# SgProp.Cells[4, 0] = 'Text'
# Refresh(Sender)
#
#
# Refresh(Sender: TObject)
# Modified  =  True
# Panel = PanelList.Items[CurrentPanel]
# with Panel:
#      if BevelOuter=bvRaised: SgProp.Cells[4, 0] = 'Caption'
#      if (BevelOuter=bvLowered)or(BevelOuter=bvNone): SgProp.Cells[4, 0] = 'Text'
#      Top = Tk
#      Height = Hk
#      Left = Lk
#      Width = Wk
#      SgProp.Cells[0, 1] = IntToStr(Left + SbDesk.HorzScrollBar.Position)
#      SgProp.Cells[1, 1] = IntToStr(Top + SbDesk.VertScrollBar.Position)
#      SgProp.Cells[2, 1] = IntToStr(Width)
#      SgProp.Cells[3, 1] = IntToStr(Height)
#      SgProp.Cells[4, 1] = Caption
#      STopLeft.Top = Top-3
#      STopLeft.Left = Left-3
#      STopCenter.Top = Top-3
#      STopCenter.Left = Left + Width div 2 - 2
#      STopRight.Top = Top-3
#      STopRight.Left = Left + Width-2
#      SMiddleLeft.Top = Top + Height div 2 -2
#      SMiddleLeft.Left = Left-3
#      SMiddleRight.Top = Top + Height div 2 -2
#      SMiddleRight.Left = Left + Width-2
#      SBottomLeft.Top = Top + Height-2
#      SBottomLeft.Left = Left-3
#      SBottomCenter.Top = Top + Height-2
#      SBottomCenter.Left = Left + Width div 2 - 2
#      SBottomRight.Top = Top + Height-2
#      SBottomRight.Left = Left + Width-2
# mnExitClick(Sender: TObject)
# Close
#
#
# mnOpenClick(Sender: TObject)
# var
#   DialogValue,i:integer
#   TempString:array[0..79] of char
#   LogName:string
# if Modified:
#      DialogValue = MessageDlg('Сохранить изменения в файле?', mtWarning, [mbYes, mbNo], 0)
#      if DialogValue=mrYes: mnSaveClick(Sender)
# if Opialog1.Execute:
#      CurrentFileName = Opialog1.FileName
#      {$I-}
#      AssignFile(F, CurrentFileName)
#      Reset(F)
#      CloseFile(F)
#      {$I + }
#      if IOResult=0:
#           Count = PanelList.Count-1
#           for i = Count:wnto 0:
#                Panel = PanelList.Items[i]
#                PanelList.Delete(i)
#                Panel.Free
#           if OpenTextFile(CurrentFileName, Prop_i, Prop_s):
#                LogName = Copy(ExtractFileName(CurrentFileName),1,Length(ExtractFileName(CurrentFileName))-4) + '.log'
#                DialogValue = MessageDlg('В конфигурации обнаружены ошибки.' + Chr(13) + Chr(10) + 'Подробности в журнале: ' +
#                LogName + Chr(13) + Chr(10) + 'Открыть ' + LogName + ' ?', mtWarning, [mbYes, mbNo], 0)
#                if DialogValue=mrYes:
#                     StrPCopy(TempString, LogName)
#                     ShellExecute(0, Nil, TempString, Nil, Nil, SW_NORMAL)
#           for i = 1 to High(Prop_s):
#                PanelList.Add(TPanel.Create(Self))
#                Count = PanelList.Count-1
#                Panel = PanelList.Items[Count]
#                with Panel:
#                     Parent = SbDesk
#                          case Prop_i[0, i] of
#                          1:
#                               BevelOuter = bvRaised
#                               Color = clBtnFace
#                               Alignment = taCenter
#
#                          2:
#                               BevelOuter = bvLowered
#                               Color = clHighlightText
#                               Alignment = taLeftJustify
#
#                          3:
#                               BevelOuter = bvNone
#                               Color = clBtnFace
#                               Alignment = taLeftJustify
#                     Tag = Count
#                     Cursor = crSizeAll
#                     BevelWidth = 2
#                     Caption = Prop_s[i]
#                     TabOrder = 0
#                     PopupMenu = PopupMenu1
#                     OnMouseDown = PanelMouseDown
#                     OnMouseMove = PanelMouseMove
#                Lk = Prop_i[1, i]-sbDesk.HorzScrollBar.Position
#                Tk = Prop_i[2, i]-sbDesk.VertScrollBar.Position
#                Wk = Prop_i[3, i]
#                Hk = Prop_i[4, i]
#                CurrentPanel = Count
#                Refresh(Sender)
#           Caption = 'Editor - ' + ExtractFileName(CurrentFileName)
#           Modified  =  False
#           SbDeskClick(Sender)
#
# mnSaveClick(Sender: TObject)
# var
#   i,p,t:integer
#   ObjectType, TextProp:string
#   Sort:array of array of integer
# Modified  =  False
# if CurrentFileName=DefaultFileName: MnSaveAsClick(Sender) else
#      Count = PanelList.Count-1
#      SetLength(Sort, 3, Count + 1)
#      for i = 0 to Count: # Подготовка массива для сортировки Top, Left
#           Sort[0,i] = i
#           Panel = PanelList.Items[i]
#           Sort[1,i] = Panel.Left
#           Sort[2,i] = Panel.Top
#      repeat # Сортировка по параметру Left
#      p = 0
#      for i = 0 to Count-1:
#           if Sort[1, i]>Sort[1, i + 1]:
#                t = Sort[0, i]
#                Sort[0, i] = Sort[0, i + 1]
#                Sort[0, i + 1] = t
#                t = Sort[1, i]
#                Sort[1, i] = Sort[1, i + 1]
#                Sort[1, i + 1] = t
#                t = Sort[2, i]
#                Sort[2, i] = Sort[2, i + 1]
#                Sort[2, i + 1] = t
#                p = p + 1
#      until p=0
#      repeat # Сортировка по параметру Top
#      p = 0
#      for i = 0 to Count-1:
#           if Sort[2, i]>Sort[2, i + 1]:
#                t = Sort[0, i]
#                Sort[0, i] = Sort[0, i + 1]
#                Sort[0, i + 1] = t
#                t = Sort[1, i]
#                Sort[1, i] = Sort[1, i + 1]
#                Sort[1, i + 1] = t
#                t = Sort[2, i]
#                Sort[2, i] = Sort[2, i + 1]
#                Sort[2, i + 1] = t
#                p = p + 1
#      until p=0
#      AssignFile(F, CurrentFileName)
#      Rewrite(F)
#      for i = 0 to Count:
#           Panel = PanelList.Items[Sort[0,i]]
#           with Panel:
#                if BevelOuter=bvRaised: ObjectType = 'Button'
#                if BevelOuter=bvLowered: ObjectType = 'TextEdit'
#                if BevelOuter=bvNone: ObjectType = 'Label'
#                if ObjectType='Button': TextProp = 'caption' else TextProp = 'text'
#                Write(F, '<' + ObjectType)
#                Write(F, ' left="' + IntToStr(Left + sbDesk.HorzScrollBar.Position) + '"')
#                Write(F, ' top="' + IntToStr(Top + sbDesk.VertScrollBar.Position) + '"')
#                Write(F, ' width="' + IntToStr(Width) + '"')
#                if ObjectType != 'TextEdit': Write(F, ' height="' + IntToStr(Height) + '"')
#                Writeln(F, ' ' + TextProp + '="' + Caption + '">')
#      CloseFile(F)
#
# mnSaveAsClick(Sender: TObject)
# var
#   DialogValue, i:integer
#   FileName:string
# FileName = CurrentFileName
# i = Pos('.', FileName)
# if i != 0: Delete(FileName, i, Length(FileName)-i + 1)
# FileName = FileName + '.txt'
# SaveDialog1.FileName  =  FileName
# SaveDialog1.Filter = 'Text files (*.txt)|*.txt|All files|*.*'
# if SaveDialog1.Execute:
#      FileName = SaveDialog1.FileName
#      i = Pos('.', FileName)
#      if i=0: FileName = FileName + '.txt'
#      DialogValue = mrYes
#      if FileExists(FileName)then DialogValue = MessageDlg('Файл ' + ExtractFileName(FileName) + ' существует. Перезаписать?', mtWarning, [mbYes, mbNo], 0)
#      if DialogValue=mrYes:
#           CurrentFileName = FileName
#           Caption = 'Editor - ' + ExtractFileName(CurrentFileName)
#           MnSaveClick(Sender)
#
# mnSaveWebClick(Sender: TObject)
# var
#   DialogValue,i,j:integer
#   HTMLFileName:string
# j = 1
# SetLength(Prop_i, 7, 1)
# SetLength(Prop_s, 1)
# for i = 0 to MainForm.ComponentCount-1: if MainForm.Components[i] is TPanel:
#      with TPanel(MainForm.Components[i]):
#      SetLength(Prop_i, 7, j + 1)
#      SetLength(Prop_s, j + 1)
#      if BevelOuter=bvRaised: Prop_i[0, j] = 1
#      if BevelOuter=bvLowered: Prop_i[0, j] = 2
#      if BevelOuter=bvNone: Prop_i[0, j] = 3
#      Prop_i[1, j] = Left + sbDesk.HorzScrollBar.Position
#      Prop_i[2, j] = Top + sbDesk.VertScrollBar.Position
#      Prop_i[3, j] = Width
#      Prop_i[4, j] = Height
#      Prop_s[j] = Caption
#      j = j + 1
# if j>1:
#      HTMLFileName = CurrentFileName
#      i = Pos('.', HTMLFileName)
#      if i != 0: Delete(HTMLFileName, i, Length(HTMLFileName)-i + 1)
#      SaveDialog1.FileName =  HTMLFileName + '.htm'
#      SaveDialog1.Filter = 'HTML files (*.htm *.html)|*.htm *.html|All files|*.*'
#      if SaveDialog1.Execute:
#           HTMLFileName = SaveDialog1.FileName
#           DialogValue = mrYes
#           if FileExists(HTMLFileName)then DialogValue = MessageDlg('Файл ' + ExtractFileName(HTMLFileName) + ' существует. Перезаписать?', mtWarning, [mbYes, mbNo], 0)
#           if DialogValue=mrYes: WriteHTMLFile(HTMLFileName, Prop_i, Prop_s)
#
# mnNewClick(Sender: TObject)
# var
#   DialogValue, i:integer
# if Modified:
#      DialogValue = MessageDlg('Сохранить изменения в файле?', mtWarning, [mbYes, mbNo], 0)
#      if DialogValue=mrYes: mnSaveClick(Sender)
# Modified = False
# CurrentFileName = DefaultFileName
# Caption = 'Editor - ' + ExtractFileName(CurrentFileName)
# Count = PanelList.Count-1
# for i = Count:wnto 0:
#      Panel = PanelList.Items[i]
#      PanelList.Delete(i)
#      Panel.Free
# SbDeskClick(Sender)
#
#
# sbCrBtnClick(Sender: TObject)
# sbCrBtn.Down = True
# NeedCreate = 1
# sbDesk.Cursor = crDrag
# SbDesk.Hint = 'Новая кнопка'
# SbDesk.ShowHint =  True
#
#
# sbCrTxtClick(Sender: TObject)
# sbCrTxt.Down = True
# NeedCreate = 2
# sbDesk.Cursor = crDrag
# SbDesk.Hint = 'Новое поле ввода'
# SbDesk.ShowHint =  True
#
#
# sbCrLabClick(Sender: TObject)
# sbCrLab.Down = True
# NeedCreate = 3
# sbDesk.Cursor = crDrag
# SbDesk.Hint = 'Новая надпись'
# SbDesk.ShowHint =  True
#
#
# pmDelClick(Sender: TObject)
# var i:integer
# Panel = PanelList.Items[CurrentPanel]
# PanelList.Delete(CurrentPanel)
# Panel.Free
# Count = PanelList.Count-1
# CurrentPanel = Count
# for i = 0 to Count:
#      Panel = PanelList.Items[i]
#      Panel.Tag = i
# SbDeskClick(Sender)
#
#
# SgPropKeyPress(Sender: TObject var Key: Char)
# if (SgProp.Col<4):
#      if Key=#8: SgProp.Cells[SgProp.Col,1] = '' else if not(Key in['0'..'9'])then Key = #0
#       else if (PanelList.Count>0):
#      Panel = PanelList.Items[CurrentPanel]
#      Panel.Caption = SgProp.Cells[4,1]
#
# SgPropKeyDown(Sender: TObject var Key: Word Shift: TShiftState)
# var i,T1,L1:integer
# if (Key=VK_RETURN) and (PanelList.Count>0):
#      Panel = PanelList.Items[CurrentPanel]
#      with Panel:
#           T1 = Top
#           L1 = Left
#           L0 = Left
#           T0 = Top
#           H0 = Height
#           W0 = Width
#           Lk = Left
#           Tk = Top
#           Hk = Height
#           Wk = Width
#      i = SgProp.Col
#           case i of
#           0:    # left
#                with sbDesk:
#
#                          try Lk = StrToInt(SgProp.Cells[0,1])-HorzScrollBar.Position
#                          except on E: EConvertError:
#                     if Lk<-HorzScrollBar.Position: Lk = -HorzScrollBar.Position + 1
#                     if Lk + Wk + HorzScrollBar.Position>HorzScrollBar.Range:
#                          Lk = HorzScrollBar.Range-Wk-HorzScrollBar.Position-1
#
#                     Count = PanelList.Count-1
#                for i = 0 to Count:
#
#                     if i != CurrentPanel:
#
#                          Panel = PanelList.Items[i]
#                          with Panel:
#
#                               if (L1>Left) and (T1 + Hk>Top) and (T1<Top + Height) and (Lk<Left + Width)then Lk = Left + Width
#                               if (L1<Left) and (T1 + Hk>Top) and (T1<Top + Height) and (Lk + Wk>Left)then Lk = Left-Wk
#
#           1:    # top
#                with sbDesk:
#                          try Tk = StrToInt(SgProp.Cells[1,1])-VertScrollBar.Position
#                          except on E: EConvertError:
#                     if Tk<-VertScrollBar.Position: Tk = -VertScrollBar.Position + 1
#                     if Tk + Hk + VertScrollBar.Position>VertScrollBar.Range:
#                          Tk = VertScrollBar.Range-Hk-VertScrollBar.Position-1
#                     Count = PanelList.Count-1
#                for i = 0 to Count:
#                     if i != CurrentPanel:
#                          Panel = PanelList.Items[i]
#                          with Panel:
#                               if (T1>Top) and (L1<Left + Width) and (L1 + Wk>Left) and (Tk<Top + Height): Tk = Top + Height
#                               if (T1<Top) and (L1<Left + Width) and (L1 + Wk>Left) and (Tk + Hk>Top): Tk = Top-Hk
#
#           2:    # width
#                     try Wk = StrToInt(SgProp.Cells[2,1])
#                     except on E: EConvertError:
#                Count = PanelList.Count-1
#                for i = 0 to Count:
#                     if i != CurrentPanel:
#                          Panel = PanelList.Items[i]
#                          with Panel: if (Lk<Left) and (Tk + Hk>Top) and (Tk<Top + Height) and (Lk + Wk>Left): Wk = Left-Lk
#
#                if Lk + Wk + SbDesk.HorzScrollBar.Position > SbDesk.HorzScrollBar.Range:
#                     Wk = SbDesk.HorzScrollBar.Range-Lk-SbDesk.HorzScrollBar.Position
#                if Wk < MinWidth: Wk = MinWidth
#           3:    # height
#                if Panel.BevelOuter != bvLowered:
#                          try Hk = StrToInt(SgProp.Cells[3,1])
#                          except on E: EConvertError:
#                     if Tk + Hk + SbDesk.VertScrollBar.Position > SbDesk.VertScrollBar.Range:
#                          Hk = SbDesk.VertScrollBar.Range-Tk-SbDesk.VertScrollBar.Position
#                     Count = PanelList.Count-1
#                     for i = 0 to Count:
#                          if i != CurrentPanel:
#                               Panel = PanelList.Items[i]
#                               with Panel: if (Tk<Top) and (Lk<Left + Width) and (Lk + Wk>Left) and (Tk + Hk>Top)then
#                                    Hk = Top-Tk
#                     if Hk < MinHeight: Hk = MinHeight
#           4:
#                Panel.Caption = SgProp.Cells[4,1]
#      Refresh(Sender)
#
# SbDeskClick(Sender: TObject)
# var i:integer
# if NeedCreate=0:
#      for i = 0 to MainForm.ComponentCount-1: if MainForm.Components[i] is TShape:
#           TShape(MainForm.Components[i]).Visible = False
#      for i = 0 to 4: SgProp.Cells[i, 1] = ''
#      mnDel.Enabled = False
#      mnDel.ShortCut = ShortCut(0, [])
#
# FormClose(Sender: TObject var Action: TCloseAction)
# var DialogValue: Integer
# if Modified:
#      DialogValue = MessageDlg('Сохранить изменения в файле?', mtWarning, [mbYes, mbNo], 0)
#      if DialogValue=mrYes: mnSaveClick(Sender)
# if FileExists('editor_tmp.htm'): DeleteFile('editor_tmp.htm')
#
# SgPropClick(Sender: TObject)
# mnDel.Enabled = False
# mnDel.ShortCut = ShortCut(0, [])
#
# sbSelectClick(Sender: TObject)
# sbDesk.Cursor = crDefault
# sbSelect.Down = True
# NeedCreate = 0
# SbDesk.ShowHint = False
#
# SbDeskMouseDown(Sender: TObject Button: TMouseButton Shift: TShiftState X, Y: Integer)
# if (NeedCreate != 0) and Valid:
#      PanelList.Add(TPanel.Create(Self))
#      Count = PanelList.Count-1
#      Panel = PanelList.Items[Count]
#      with Panel:
#           Parent = SbDesk
#           Tag = Count
#           Cursor = crSizeAll
#           BevelWidth = 2
#           PopupMenu = PopupMenu1
#           OnMouseDown = PanelMouseDown
#           OnMouseUp = PanelMouseDown
#           OnMouseMove = PanelMouseMove
#      Lk = X
#      Tk = Y
#      Wk = DefaultWidth
#      Hk = DefaultHeight
#           case NeedCreate of
#           1:
#                SgProp.Cells[4, 0] = 'Caption'
#                with Panel:
#                     BevelOuter = bvRaised
#                     Color = clBtnFace
#                     Alignment = taCenter
#                     Caption = 'Button' + IntToStr(Count)
#           2:
#                SgProp.Cells[4, 0] = 'Text'
#                with Panel:
#
#                     BevelOuter = bvLowered
#                     Color = clHighlightText
#                     Alignment = taLeftJustify
#                     Caption = 'TextEdit' + IntToStr(Count)
#           3:
#                SgProp.Cells[4, 0] = 'Text'
#                with Panel:
#
#                     BevelOuter = bvNone
#                     Color = clBtnFace
#                     Alignment = taLeftJustify
#                     Caption = 'Label' + IntToStr(Count)
#      sbSelectClick(Sender)
#      CurrentPanel = Count
#      Refresh(Sender)
#
# SbDeskMouseMove(Sender: TObject Shift: TShiftState X, Y: Integer)
# var
#   i:integer
# if NeedCreate != 0:
#           i = 0
#           Valid = True
#           repeat
#           if MainForm.Components[i] is TPanel: with TPanel(MainForm.Components[i]):
#           if (Y + DefaultHeight>Top) and (Y<Top + Height) and (X + DefaultWidth>Left) and (X<Left + Width)then Valid = False
#           i = i + 1
#           until (Valid=False)or(i=MainForm.ComponentCount)
#      if Valid:
#           sbDesk.Cursor = crDrag
#           SbDesk.ShowHint = True
#            else
#           sbDesk.Cursor = crNoDrop
#           SbDesk.ShowHint = False
#
# mnViewWebClick(Sender: TObject)
# var
# TempString : array[0..79] of char
# i,j:integer
# j = 1
# SetLength(Prop_i, 7, 1)
# SetLength(Prop_s, 1)
# for i = 0 to MainForm.ComponentCount-1: if MainForm.Components[i] is TPanel:
#      with TPanel(MainForm.Components[i]):
#      SetLength(Prop_i, 7, j + 1)
#      SetLength(Prop_s, j + 1)
#      if BevelOuter=bvRaised: Prop_i[0, j] = 1
#      if BevelOuter=bvLowered: Prop_i[0, j] = 2
#      if BevelOuter=bvNone: Prop_i[0, j] = 3
#      Prop_i[1, j] = Left + sbDesk.HorzScrollBar.Position
#      Prop_i[2, j] = Top + sbDesk.VertScrollBar.Position
#      Prop_i[3, j] = Width
#      Prop_i[4, j] = Height
#      Prop_s[j] = Caption
#      j = j + 1
# if j>1:
#      WriteHTMLFile('editor_tmp.htm', Prop_i, Prop_s)
#      StrPCopy(TempString, 'editor_tmp.htm')
#      ShellExecute(0, Nil, TempString, Nil, Nil, SW_NORMAL)
#
