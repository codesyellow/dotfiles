/* See LICENSE file for copyright and license details. */

/* appearance */
static const unsigned int borderpx  = 4;        /* border pixel of windows */
static const unsigned int snap      = 32;       /* snap pixel */
static const unsigned int gappih    = 20;       /* horiz inner gap between windows */
static const unsigned int gappiv    = 10;       /* vert inner gap between windows */
static const unsigned int gappoh    = 10;       /* horiz outer gap between windows and screen edge */
static const unsigned int gappov    = 30;       /* vert outer gap between windows and screen edge */
static       int smartgaps          = 1;        /* 1 means no outer gap when there is only one window */
static const unsigned int systraypinning = 0;   /* 0: sloppy systray follows selected monitor, >0: pin systray to monitor X */
static const unsigned int systrayonleft  = 0;   /* 0: systray in the right corner, >0: systray on left of status text */
static const unsigned int systrayspacing = 2;   /* systray spacing */
static const int systraypinningfailfirst = 1;   /* 1: if pinning fails, display systray on the first monitor, False: display systray on the last monitor*/
static const int showsystray        = 1;        /* 0 means no systray */
static const int showbar            = 1;        /* 0 means no bar */
static const int topbar             = 1;        /* 0 means bottom bar */
static const char *fonts[]          = { 
  "CaskadiaCove Nerd Font:size=10",
  "Font Awesome 6 Free Solid:size=10",
  "Font Awesome 6 Free Regular:size=10",
  "Font Awesome 6 Brands:size=10"
   };
static const char dmenufont[]       = "monospace:size=10";
static const char col_gray1[]       = "#222222";
static const char col_gray2[]       = "#444444";
static const char col_gray3[]       = "#bbbbbb";
static const char col_gray4[]       = "#eeeeee";
static const char col_cyan[]        = "#005577";
static const char *colors[][3]      = {
  /*               fg         bg         border   */
  [SchemeNorm] = { col_gray3, col_gray1, col_gray2 },
  [SchemeSel]  = { col_gray4, col_cyan,  col_cyan  },
};

/* tagging */
static const char *tags[] = { "1", "2", "3", "4", "5" };

static const Rule rules[] = {
  /* xprop(1):
   *	WM_CLASS(STRING) = instance, class
   *	WM_NAME(STRING) = title
   */
  /* class      instance    title       tags mask     isfloating   monitor    float x,y,w,h         floatborderpx*/
  { "Gimp",     NULL,       NULL,       0,            1,           -1,        50,50,500,500,        5 },
  { "org.mozilla.firefox",  NULL,       NULL,       1 << 0,       0,           -1,        50,50,500,500,        5,      0},
  { "Firefox",  NULL,       NULL,       1 << 0,       0,           -1,        50,50,500,500,        5,      0},
  { "Alacritty",  NULL,       NULL,       1 << 1,       0,           -1,        50,50,500,500,        5,      0},
  { "Zathura",  NULL,       NULL,       1 << 2,       0,           -1,        50,50,500,500,        5,      0},
  { "steam",  NULL,       NULL,       1 << 3,       0,           -1,        50,50,500,500,        5,      0},
  { "heroic",  NULL,       NULL,       1 << 3,       0,           -1,        50,50,500,500,        5,      0},
  { "Youtube Music",  NULL,       NULL,       1 << 4,       0,           -1,        50,50,500,500,        5,      0},
  /* class      instance    title       tags mask     isfloating   monitor    scratch key */
  { NULL,       NULL,   "scratchpad",   0,            1,           -1,   's', 50,50,500,500,        5,   },
  { NULL,       NULL,   "btop",   0,            1,           -1,   'b', 50,50,1200,500,        5,   },

};

/* layout(s) */
static const float mfact     = 0.90; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 1;    /* 1 means respect size hints in tiled resizals */
static const int lockfullscreen = 1; /* 1 will force focus on the fullscreen window */
#define FORCE_VSPLIT 1  /* nrowgrid layout: force two clients to always split vertically */
#include "vanitygaps.c"

static const Layout layouts[] = {
  /* symbol     arrange function */
	{ ">M>",      centeredfloatingmaster },
  { "[]=",      tile },    /* first entry is default */
  { "><>",      NULL },    /* no layout function means floating behavior */
  { "[M]",      monocle },
	{ "|M|",      centeredmaster },
};

/* key definitions */
#define MODKEY Mod4Mask
#define TAGKEYS(KEY,TAG)                                                                                               \
&((Keychord){1, {{MODKEY, KEY}},                                        view,           {.ui = 1 << TAG} }), \
&((Keychord){1, {{MODKEY|ControlMask, KEY}},                            toggleview,     {.ui = 1 << TAG} }), \
&((Keychord){1, {{MODKEY|ShiftMask, KEY}},                              tag,            {.ui = 1 << TAG} }), \
&((Keychord){1, {{MODKEY|ControlMask|ShiftMask, KEY}},                  toggletag,      {.ui = 1 << TAG} }),
/* helper for spawning shell commands in the pre dwm-5.0 fashion */
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

/* commands */
static char dmenumon[2] = "0"; /* component of dmenucmd, manipulated in spawn() */
static const char *dmenucmd[] = { "dmenu_run", "-m", dmenumon, "-fn", dmenufont, "-nb", col_gray1, "-nf", col_gray3, "-sb", col_cyan, "-sf", col_gray4, NULL };
static const char *bass[] = { "flatpak", "run", "com.github.wwmm.easyeffects", "-l", "my-heavy-bass", NULL};
static const char *loudness[] = { "flatpak", "run", "com.github.wwmm.easyeffects", "-l", "LoudnessEqualizer", NULL};
static const char *termcmd[]  = { "alacritty", NULL };
/*First arg only serves to match against key in rules*/
static const char *scratchpadcmd[] = {"s", "st", "-t", "scratchpad", NULL}; 
static const char *scratchpadbtop[] = {"b", "st", "-t", "btop", "-e", "btop", NULL}; 


#include "movestack.c"
static Keychord *keychords[] = {
  /* Keys        function        argument */
  // exec
  &((Keychord){2, {{MODKEY, XK_e}, {0, XK_r}},                                       spawn,          {.v = dmenucmd } }),
  &((Keychord){3, {{MODKEY, XK_e}, {0, XK_e}, {0, XK_b}},                                       spawn,          {.v = bass } }),
  &((Keychord){3, {{MODKEY, XK_e}, {0, XK_e}, {0, XK_l}},                                       spawn,          {.v = loudness } }),
  // action
    // layouts
  &((Keychord){4, {{MODKEY, XK_a}, {0, XK_c}, {0, XK_l}, {0, XK_1}},                                       setlayout,      {.v = &layouts[0]} }),
  &((Keychord){4, {{MODKEY, XK_a}, {0, XK_c}, {0, XK_l}, {0, XK_2}},                                       setlayout,      {.v = &layouts[1]} }),
  &((Keychord){4, {{MODKEY, XK_a}, {0, XK_c}, {0, XK_l}, {0, XK_3}},                                       setlayout,      {.v = &layouts[2]} }),
  &((Keychord){4, {{MODKEY, XK_a}, {0, XK_c}, {0, XK_l}, {0, XK_4}},                                       setlayout,      {.v = &layouts[4]} }),
  &((Keychord){3, {{MODKEY, XK_a}, {0, XK_c}, {0, XK_f}},        togglefullscr,  {0}}),

  &((Keychord){1, {{MODKEY, XK_j}},                                       movestack,     {.i = +1 } }),
  &((Keychord){1, {{MODKEY, XK_k}},                                       movestack,     {.i = -1 } }),
  // scratch
  &((Keychord){2, {{MODKEY, XK_v}, {0, XK_j}},                            spawn,          SHCMD("volume.sh down")}),
  &((Keychord){2, {{MODKEY, XK_v}, {0, XK_k}},                            spawn,          SHCMD("volume.sh up")}),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_u}},                            togglescratch,  {.v = scratchpadcmd } }),
  &((Keychord){2, {{MODKEY, XK_s}, {0, XK_b}},                            togglescratch,  {.v = scratchpadbtop } }),
  // normal
  &((Keychord){1, {{MODKEY, XK_t}},                                       spawn,          {.v = termcmd } }),
  &((Keychord){1, {{MODKEY, XK_b}},                                       togglebar,      {0} }),
  &((Keychord){1, {{MODKEY, XK_j}},                                       focusstack,     {.i = +1 } }),
  &((Keychord){1, {{MODKEY, XK_k}},                                       focusstack,     {.i = -1 } }),
  &((Keychord){1, {{MODKEY, XK_i}},                                       incnmaster,     {.i = +1 } }),
  &((Keychord){1, {{MODKEY, XK_d}},                                       incnmaster,     {.i = -1 } }),
  &((Keychord){1, {{MODKEY, XK_h}},                                       setmfact,       {.f = -0.05} }),
  &((Keychord){1, {{MODKEY, XK_l}},                                       setmfact,       {.f = +0.05} }),
  &((Keychord){1, {{MODKEY, XK_Return}},                                  zoom,           {0} }),
  &((Keychord){1, {{MODKEY, XK_Tab}},                                     view,           {0} }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_c}},                             killclient,     {0} }),
  &((Keychord){1, {{MODKEY, XK_space}},                                   setlayout,      {0} }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_space}},                         togglefloating, {0} }),
  &((Keychord){1, {{MODKEY, XK_0}},                                       view,           {.ui = ~0 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_0}},                             tag,            {.ui = ~0 } }),
  &((Keychord){1, {{MODKEY, XK_comma}},                                   focusmon,       {.i = -1 } }),
  &((Keychord){1, {{MODKEY, XK_period}},                                  focusmon,       {.i = +1 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_comma}},                         tagmon,         {.i = -1 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_period}},                        tagmon,         {.i = +1 } }),
  &((Keychord){1, {{MODKEY|ShiftMask, XK_q}},                             quit,           {0} }),
  TAGKEYS(                        XK_1,                      0)
  TAGKEYS(                        XK_2,                      1)
  TAGKEYS(                        XK_3,                      2)
  TAGKEYS(                        XK_4,                      3)
  TAGKEYS(                        XK_5,                      4)
  TAGKEYS(                        XK_6,                      5)
  TAGKEYS(                        XK_7,                      6)
  TAGKEYS(                        XK_8,                      7)
  TAGKEYS(                        XK_9,                      8)
};

/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static const Button buttons[] = {
  /* click                event mask      button          function        argument */
  { ClkLtSymbol,          0,              Button1,        setlayout,      {0} },
  { ClkLtSymbol,          0,              Button3,        setlayout,      {.v = &layouts[2]} },
  { ClkStatusText,        0,              Button2,        spawn,          {.v = termcmd } },
  { ClkClientWin,         MODKEY,         Button1,        movemouse,      {0} },
  { ClkClientWin,         MODKEY,         Button2,        togglefloating, {0} },
  { ClkClientWin,         MODKEY,         Button3,        resizemouse,    {0} },
  { ClkTagBar,            0,              Button1,        view,           {0} },
  { ClkTagBar,            0,              Button3,        toggleview,     {0} },
  { ClkTagBar,            MODKEY,         Button1,        tag,            {0} },
  { ClkTagBar,            MODKEY,         Button3,        toggletag,      {0} },
};
