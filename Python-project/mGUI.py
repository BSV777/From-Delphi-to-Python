#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Сюда перенесены и частично преобразованы из формата Delphi некоторые функции GUI, которые должны быть реализованы в проекте

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
