##
## LCARS GUI Objects Library : Rectangular bar capped with semicircle(s)
##

from __future__ import division

import pygame

from LCARS.Controls import CappedBar, Text, TextAlign

def glow_colour(clr):
	glow = pygame.Color(clr.r, clr.g, clr.b, clr.a)
	hsla = glow.hsla
	glow.hsla = (hsla[0], hsla[1], hsla[2]*1.5, hsla[3])
	return glow

class Button(CappedBar):
	def __init__(self, rect, caplocation, text, fg, bg, textclr):
		self.glow = glow_colour(fg)
		self.is_glowing = False
		CappedBar.__init__(self, rect, caplocation, text, fg, bg, textclr)

	def setGlowText(self, text):
		self.glowtext = None
		if self.text:
			self.glowtext = Text(self.text.alignpoint, text, self.text.fontsize, self.text.xalign, self.textclr, self.glow)

	def setText(self, text):
		CappedBar.setText(self, text)
		self.setGlowText(text)

	def _onmousedown(self, event):
		self.is_glowing = True
		self.onmousedown(event)

	def _onmouseup(self, event):
		self.is_glowing = False
		self.onmouseup(event)

	def _ondragout(self, event, target):
		self.is_glowing = False
		self.ondragout(event, target)

	def _ondragin(self, event, target):
		self.is_glowing = (target==self)
		self.ondragin(event, target)

	def draw(self, window):
		if not self.visible: return
		oldclr = self.fg
		oldtext = self.text
		if self.is_glowing:
			self.fg = self.glow
			self.text = self.glowtext
		try:
			CappedBar.draw(self, window)
		except:
			pass
		self.fg = oldclr
		self.text = oldtext