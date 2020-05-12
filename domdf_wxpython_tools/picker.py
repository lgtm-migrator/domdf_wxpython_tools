#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  picker.py
#
#  Copyright 2019 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
# generated by wxGlade 0.9.3 on Thu Jun  6 12:07:28 2019
#

# stdlib
import pathlib

# 3rd party
import wx

# this package
from domdf_wxpython_tools.dialogs import file_dialog
from domdf_wxpython_tools.textctrlwrapper import TextCtrlWrapper
from . import icons


# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class dir_picker(TextCtrlWrapper, wx.Panel):
	"""
	
	"""
	def __init__(
			self, parent, id=wx.ID_ANY, value="", pos=wx.DefaultPosition,
			size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=b"dir_picker",
			):
		"""
		
		:param parent:
		:type parent:
		:param id:
		:type id:
		:param value:
		:type value:
		:param pos:
		:type pos:
		:param size:
		:type size:
		:param style:
		:type style:
		:param name:
		:type name:
		"""
		
		self._parent = parent
		self.initial_value = value
		
		wx.Panel.__init__(self, self._parent, id=id, pos=pos, size=size, style=style, name=name)
		self.textctrl = self.dir_value = wx.TextCtrl(self, wx.ID_ANY, "")
		self.clear_btn = wx.BitmapButton(self, wx.ID_ANY, icons.get_button_icon("ART_GO_BACK", 16))
		self.browse_btn = wx.BitmapButton(self, wx.ID_ANY, icons.get_button_icon("ART_FOLDER_OPEN", 16))
		
		self.textctrl_width = 150
		self.height = 29
		
		self.__set_properties()
		self.__do_layout()
		
		self.Bind(wx.EVT_BUTTON, self.Clear, self.clear_btn)
		self.Bind(wx.EVT_BUTTON, self.Browse, self.browse_btn)
		
	def __set_properties(self):
		# begin wxGlade: dir_picker.__set_properties
		self.dir_value.SetMinSize((-1, 29))
		self.dir_value.SetMaxSize((-1, 29))
		self.clear_btn.SetMinSize((29, 29))
		self.browse_btn.SetMinSize((29, 29))
		# end wxGlade
		# self.dir_value.SetMinSize((self.textctrl_width, self.height))
		# self.clear_btn.SetMinSize((self.height, self.height))
		# self.browse_btn.SetMinSize((self.height, self.height))
		# self.SetMinSize((self.textctrl_width + 5 + (2*self.height), self.height+5))
	
	def __do_layout(self):
		# begin wxGlade: dir_picker.__do_layout
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer_5 = wx.BoxSizer(wx.VERTICAL)
		sizer_5.Add(self.dir_value, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		sizer.Add(sizer_5, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		sizer.Add(self.clear_btn, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		sizer.Add(self.browse_btn, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		self.SetSizer(sizer)
		sizer.Fit(self)
		self.Layout()
		# end wxGlade
	
	def set_textctrl_width(self, width):
		self.SetTextWidth(width)
	
	def set_height(self, height):
		self.SetHeight(height)
		
	def get_value(self):
		return self.GetValue()
	
	def reset_value(self):
		return self.ResetValue()

	def Browse(self, *_):  # wxGlade: dir_picker.<event_handler>
		if self.get_value() == '':
			default_path = self.initial_value
		else:
			default_path = self.get_value()
		
		dlg = wx.DirDialog(
			None, "Choose a directory:",
			style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON,
			defaultPath=default_path
		)
		
		if dlg.ShowModal() == wx.ID_OK:
			self.dir_value.SetValue((dlg.GetPath()))
		dlg.Destroy()
		self.dir_value.SetFocus()

	def Clear(self, *_):  # wxGlade: dir_picker.<event_handler>
		"""
		Clears the text in the control.

		Note that this function will generate a wxEVT_TEXT event, i.e. its effect is identical to calling SetValue (“”).
		"""
		self.dir_value.Clear()
		self.dir_value.SetFocus()

	def GetInsertionPoint(self):
		"""
		Returns the insertion point, or cursor, position.
	
		This is defined as the zero based index of the character position to the right of the insertion point. For example, if the insertion point is at the end of the single-line text control, it is equal to GetLastPosition .
	
		:rtype:	long
		"""
		return self.dir_value.GetInsertionPoint()

	def ResetValue(self):
		"""
		Resets the text ctrl to the initial value, either specified in __init__ or set with SetInitialValue
		"""
		return self.dir_value.SetValue(self.initial_value)

	def SetHeight(self, height):
		"""
		Set the height of the widgets
		
		:param height: Height of the widgets
		:type height: float or int
		"""
		self.height = height
		self.__set_properties()
		self.Layout()

	def SetInitialValue(self, value):
		"""
		Sets the initial value for the text ctrl
		
		:param value: Initial value for the text ctrl
		:type value: string
		"""
		self.initial_value = value
		
	def SetInsertionPoint(self, pos):
		"""
		Sets the insertion point at the given position.
		
		:param pos: Position to set, in the range from 0 to GetLastPosition inclusive.
		:type pos: long
		:return:
		"""
		return self.dir_value.SetInsertionPoint(pos)

	def SetInsertionPointEnd(self):
		"""
		Sets the insertion point at the end of the text control.
		
		This is equivalent to calling wx.TextCtrl.SetInsertionPoint with wx.TextCtrl.GetLastPosition argument.
		"""
		return self.dir_value.SetInsertionPointEnd()

	def SetTextWidth(self, width):
		"""
		Sets the width of the TextCtrl
		
		:param width: The width of the TextCtrl
		:type width: float or int
		"""
		
		self.textctrl_width = width
		self.__set_properties()
		self.Layout()
	
# end of class dir_picker


class file_picker(dir_picker):
	"""

	"""
	
	def __init__(
			self, parent, id=wx.ID_ANY, value="", pos=wx.DefaultPosition, size=wx.DefaultSize,
			style=wx.TAB_TRAVERSAL | wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, name=b"file_picker",
			extension="*", title="File Picker", filetypestring="All Files", **kwargs
	):
		"""

		:param parent:
		:type parent:
		:param id:
		:type id:
		:param value:
		:type value:
		:param pos:
		:type pos:
		:param size:
		:type size:
		:param style:
		:type style:
		:param name:
		:type name:
		:param extension:
		:type extension:
		:param title:
		:type title:
		:param filetypestring:
		:type filetypestring:
		:param kwargs:
		:type kwargs:
		"""
		
		self._parent = parent
		self.initial_value = value
		self.file_extension = extension
		self.dialog_title = title
		self.filetypestring = filetypestring
		self.file_dialog_kwargs = kwargs
		self.style = style
		
		dir_picker.__init__(self, parent, id, value, pos, size, style, name)
	
	def Browse(self, *_):  # wxGlade: dir_picker.<event_handler>
		if self.get_value() == '':
			default_path = str(pathlib.Path(self.initial_value).parent)
		else:
			default_path = pathlib.Path(self.get_value())
			if default_path.is_file():
				default_path = default_path.parent
			default_path = str(default_path)
		
		pathname = file_dialog(
			self, extension=self.file_extension,
			style=self.style,
			defaultDir=default_path,
			filetypestring=self.filetypestring,
			title=self.dialog_title,
		)
		
		if pathname:
			self.dir_value.SetValue(pathname)
			self.dir_value.SetFocus()

# end of class file_picker


class file_folder_picker(dir_picker):
	"""
	
	"""
	
	def __init__(
			self, parent, id=wx.ID_ANY, value="", pos=wx.DefaultPosition, size=wx.DefaultSize,
			style=wx.TAB_TRAVERSAL | wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT, name=b"file_picker",
			extension="*", title="File Picker", filetypestring="All Files", start_as_files=True, **kwargs
	):
		"""

		:param parent:
		:type parent:
		:param id:
		:type id:
		:param value:
		:type value:
		:param pos:
		:type pos:
		:param size:
		:type size:
		:param style:
		:type style:
		:param name:
		:type name:
		:param extension:
		:type extension:
		:param title:
		:type title:
		:param filetypestring:
		:type filetypestring:
		:param kwargs:
		:type kwargs:
		"""
		
		self._parent = parent
		self.initial_value = value
		self.file_extension = extension
		self.dialog_title = title
		self.filetypestring = filetypestring
		self.file_dialog_kwargs = kwargs
		self.style = style
		self.files_mode = start_as_files
		
		dir_picker.__init__(self, parent, id, value, pos, size, style, name)
	
	def set_folders_mode(self):
		self.files_mode = False
	
	def set_files_mode(self):
		self.files_mode = True
	
	def toggle_mode(self):
		self.files_mode = not self.files_mode
		
	def Browse(self, *_):  # wxGlade: dir_picker.<event_handler>
		
		if self.files_mode:
		
			if self.get_value() == '':
				default_path = str(pathlib.Path(self.initial_value).parent)
			else:
				default_path = pathlib.Path(self.get_value())
				if default_path.is_file():
					default_path = default_path.parent
				default_path = str(default_path)
			
			pathname = file_dialog(
				self, extension=self.file_extension,
				style=self.style,
				defaultDir=default_path,
				filetypestring=self.filetypestring,
				title=self.dialog_title,
			)
			
			if pathname:
				self.dir_value.SetValue(pathname)
				self.dir_value.SetFocus()
	
		else:
			if self.get_value() == '':
				default_path = self.initial_value
			else:
				default_path = self.get_value()
			
			dlg = wx.DirDialog(
				None, "Choose a directory:",
				style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON,
				defaultPath=default_path
			)
			
			if dlg.ShowModal() == wx.ID_OK:
				self.dir_value.SetValue((dlg.GetPath()))
			dlg.Destroy()
			self.dir_value.SetFocus()
