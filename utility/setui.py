import pyqtgraph
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
# from utility import syntax
from utility.static import CustomViewBox
from utility.setting import qfont12, qfont14, style_bc_st, style_bc_bt, style_bc_dk, style_fc_bt, style_pgbar, \
    columns_tt, columns_td, columns_tj, columns_jg, columns_gj_, columns_cj, columns_dt, columns_dd, columns_nt, \
    columns_nd, ICON_PATH, style_bc_by, style_bc_sl, columns_hj, columns_hc, columns_hg, style_fc_dk

class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.setWidth(40)
        s.setHeight(40)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt)
            painter.restore()


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.setTabPosition(QtWidgets.QTabWidget.West)

class ProxyStyle(QtWidgets.QProxyStyle):
    def drawControl(self, element, opt, painter, widget=None):
        if element == QtWidgets.QStyle.CE_TabBarTabLabel:
            ic = self.pixelMetric(QtWidgets.QStyle.PM_TabBarIconSize)
            r = QtCore.QRect(opt.rect)
            w = 0 if opt.icon.isNull() else opt.rect.width() + ic
            r.setHeight(opt.fontMetrics.width(opt.text) + w)
            r.moveBottom(opt.rect.bottom())
            opt.rect = r
        QtWidgets.QProxyStyle.drawControl(self, element, opt, painter, widget)


def SetUI(self):

    def setPushbutton(name, box=None, click=None, cmd=None, icon=None, tip=None, color=0):
        if box is not None:
            pushbutton = QtWidgets.QPushButton(name, box)
        else:
            pushbutton = QtWidgets.QPushButton(name, self)
        if color == 0:
            pushbutton.setStyleSheet(style_bc_bt)
        elif color == 1:
            pushbutton.setStyleSheet(style_bc_st)
        elif color == 2:
            pushbutton.setStyleSheet(style_bc_by)
        elif color == 3:
            pushbutton.setStyleSheet(style_bc_sl)
        pushbutton.setFont(qfont12)
        if click is not None:
            if cmd is not None:
                pushbutton.clicked.connect(lambda: click(cmd))
            else:
                pushbutton.clicked.connect(click)
        if icon is not None:
            pushbutton.setIcon(icon)
        if tip is not None:
            pushbutton.setToolTip(tip)
        return pushbutton

    def setTextEdit(tab):
        textedit = QtWidgets.QTextEdit(tab)
        textedit.setReadOnly(True)
        textedit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        textedit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        textedit.setStyleSheet(style_bc_dk)
        return textedit

    icon_main = QtGui.QIcon(f'{ICON_PATH}/python.png')
    icon_stock = QtGui.QIcon(f'{ICON_PATH}/stock.png')
    icon_coin = QtGui.QIcon(f'{ICON_PATH}/coin.png')
    icon_set = QtGui.QIcon(f'{ICON_PATH}/set.png')
    icon_log = QtGui.QIcon(f'{ICON_PATH}/log.png')
    icon_total = QtGui.QIcon(f'{ICON_PATH}/total.png')
    icon_start = QtGui.QIcon(f'{ICON_PATH}/start.png')
    icon_zoom = QtGui.QIcon(f'{ICON_PATH}/zoom.png')
    icon_dbdel = QtGui.QIcon(f'{ICON_PATH}/dbdel.png')
    icon_accdel = QtGui.QIcon(f'{ICON_PATH}/accdel.png')
    icon_stocks = QtGui.QIcon(f'{ICON_PATH}/stocks.png')
    icon_coins = QtGui.QIcon(f'{ICON_PATH}/coins.png')

    self.setFont(qfont12)
    self.setWindowTitle('BROKER & VI INFO Crawler')

    self.main_tabWidget = TabWidget(self)
    # self.st_tab = QtWidgets.QWidget()
    # self.ct_tab = QtWidgets.QWidget()
    # self.ss_tab = QtWidgets.QWidget()
    # self.cs_tab = QtWidgets.QWidget()
    self.lg_tab = QtWidgets.QWidget()
    # self.sj_tab = QtWidgets.QWidget()

    # self.main_tabWidget.addTab(self.st_tab, '')
    # self.main_tabWidget.addTab(self.ct_tab, '')
    # self.main_tabWidget.addTab(self.ss_tab, '')
    # self.main_tabWidget.addTab(self.cs_tab, '')
    self.main_tabWidget.addTab(self.lg_tab, '')
    # self.main_tabWidget.addTab(self.sj_tab, '')
    # self.main_tabWidget.setTabIcon(0, icon_stock)
    # self.main_tabWidget.setTabIcon(1, icon_coin)
    # self.main_tabWidget.setTabIcon(2, icon_stocks)
    # self.main_tabWidget.setTabIcon(3, icon_coins)
    self.main_tabWidget.setTabIcon(0, icon_log)
    # self.main_tabWidget.setTabIcon(5, icon_set)
    # self.main_tabWidget.setTabToolTip(0, '  주식 트레이더')
    # self.main_tabWidget.setTabToolTip(1, '  코인 트레이더')
    # self.main_tabWidget.setTabToolTip(2, '  주식 전략 설정')
    # self.main_tabWidget.setTabToolTip(3, '  코인 전략 설정')
    self.main_tabWidget.setTabToolTip(0, '  로그')
    # self.main_tabWidget.setTabToolTip(5, '  설정')

    # self.tt_pushButton = setPushbutton('', icon=icon_total, tip='  수익집계')
    # self.ms_pushButton = setPushbutton('', icon=icon_start, tip='  주식수동시작')
    # self.zo_pushButton = setPushbutton('', icon=icon_zoom, tip='  축소확대')
    # self.dd_pushButton = setPushbutton('', icon=icon_dbdel, tip='  거래목록 데이터 삭제 및 초기화')
    # self.sd_pushButton = setPushbutton('', icon=icon_accdel, tip='  모든 계정 설정 삭제 및 초기화')
    self.qs_pushButton = setPushbutton('', click=self.ShowQsize)
    # self.ct_pushButton = setPushbutton('', click=self.ShowDialogChart)
    # self.hg_pushButton = setPushbutton('', click=self.ShowDialogHoga)
    # self.tt_pushButton.setShortcut('Alt+T')
    # self.ms_pushButton.setShortcut('Alt+S')
    # self.zo_pushButton.setShortcut('Alt+Z')
    # self.dd_pushButton.setShortcut('Alt+X')
    # self.sd_pushButton.setShortcut('Alt+A')
    self.qs_pushButton.setShortcut('Alt+Q')
    # self.ct_pushButton.setShortcut('Alt+C')
    # self.hg_pushButton.setShortcut('Alt+H')

    # self.progressBar = QtWidgets.QProgressBar(self)
    # self.progressBar.setAlignment(Qt.AlignCenter)
    # self.progressBar.setOrientation(Qt.Vertical)
    # self.progressBar.setRange(0, 100)
    # self.progressBar.setStyleSheet(style_pgbar)

    # self.stt_tableWidget = setTablewidget(self.st_tab, columns_tt, 1)
    # self.std_tableWidget = setTablewidget(self.st_tab, columns_td, 13)
    # self.stj_tableWidget = setTablewidget(self.st_tab, columns_tj, 1)
    # self.sjg_tableWidget = setTablewidget(self.st_tab, columns_jg, 13)
    # self.sgj_tableWidget = setTablewidget(self.st_tab, columns_gj_, 15)
    # self.scj_tableWidget = setTablewidget(self.st_tab, columns_cj, 15)

    # self.setFixedSize(1403, 763)
    self.setFixedSize(800, 763)
    self.geometry().center()
    # self.main_tabWidget.setGeometry(5, 5, 1393, 753)
    self.main_tabWidget.setGeometry(5, 5, 790, 753)
 

    self.st_textEdit = setTextEdit(self.lg_tab)
    # self.ct_textEdit = setTextEdit(self.lg_tab)
    self.sc_textEdit = setTextEdit(self.lg_tab)
    # self.cc_textEdit = setTextEdit(self.lg_tab)

    # self.tt_pushButton.setGeometry(5, 250, 35, 32)
    # self.ms_pushButton.setGeometry(5, 287, 35, 32)
    # self.zo_pushButton.setGeometry(5, 324, 35, 32)
    # self.progressBar.setGeometry(6, 361, 33, 320)
    # self.progressBar.setGeometry(0, 0, 0, 0)
    # self.dd_pushButton.setGeometry(5, 687, 35, 32)
    # self.sd_pushButton.setGeometry(5, 724, 35, 32)
    self.qs_pushButton.setGeometry(0, 0, 0, 0)
    # self.ct_pushButton.setGeometry(0, 0, 0, 0)
    # self.hg_pushButton.setGeometry(0, 0, 0, 0)

    # self.stt_tableWidget.setGeometry(5, 5, 668, 42)
    # self.std_tableWidget.setGeometry(5, 52, 668, 320)
    # self.stj_tableWidget.setGeometry(5, 377, 668, 42)
    # self.sjg_tableWidget.setGeometry(5, 424, 668, 320)
    # self.sgj_tableWidget.setGeometry(678, 5, 668, 367)
    # self.scj_tableWidget.setGeometry(678, 377, 668, 367)

    self.st_textEdit.setGeometry(5, 5, 768, 367)
    # self.ct_textEdit.setGeometry(678, 5, 668, 367)
    self.sc_textEdit.setGeometry(5, 377, 768, 367)
    # self.cc_textEdit.setGeometry(678, 377, 668, 367)

    # self.s_calendarWidget.setGeometry(5, 5, 668, 245)
    # self.sdt_tableWidget.setGeometry(5, 255, 668, 42)
    # self.sds_tableWidget.setGeometry(5, 302, 668, 442)

    # self.snt_pushButton_01.setGeometry(678, 5, 219, 30)
    # self.snt_pushButton_02.setGeometry(902, 5, 219, 30)
    # self.snt_pushButton_03.setGeometry(1126, 5, 220, 30)
    # self.snt_tableWidget.setGeometry(678, 40, 668, 42)
    # self.sns_tableWidget.setGeometry(678, 87, 668, 657)

    # self.ctt_tableWidget.setGeometry(5, 5, 668, 42)
    # self.ctd_tableWidget.setGeometry(5, 52, 668, 320)
    # self.ctj_tableWidget.setGeometry(5, 377, 668, 42)
    # self.cjg_tableWidget.setGeometry(5, 424, 668, 320)
    # self.cgj_tableWidget.setGeometry(678, 5, 668, 367)
    # self.ccj_tableWidget.setGeometry(678, 377, 668, 367)

    # self.c_calendarWidget.setGeometry(5, 5, 668, 245)
    # self.cdt_tableWidget.setGeometry(5, 255, 668, 42)
    # self.cds_tableWidget.setGeometry(5, 302, 668, 442)

    # self.cnt_pushButton_01.setGeometry(678, 5, 219, 30)
    # self.cnt_pushButton_02.setGeometry(902, 5, 219, 30)
    # self.cnt_pushButton_03.setGeometry(1126, 5, 220, 30)
    # self.cnt_tableWidget.setGeometry(678, 40, 668, 42)
    # self.cns_tableWidget.setGeometry(678, 87, 668, 657)

    # self.sj_groupBox_01.setGeometry(5, 10, 1341, 120)
    # self.sj_groupBox_02.setGeometry(5, 150, 1341, 90)
    # self.sj_groupBox_03.setGeometry(5, 260, 1341, 65)
    # self.sj_groupBox_04.setGeometry(5, 345, 1341, 65)
    # self.sj_groupBox_05.setGeometry(5, 430, 1341, 90)
    # self.sj_groupBox_06.setGeometry(5, 540, 1341, 90)
    # self.sj_textEdit.setGeometry(5, 640, 1341, 103)

    # self.ss_textEdit_01.setGeometry(5, 5, 1000, 463)
    # self.ss_textEdit_02.setGeometry(5, 473, 1000, 270)
    # self.ss_textEdit_03.setGeometry(5, 5, 1000, 738)

    # self.ssb_comboBox.setGeometry(1010, 5, 165, 25)
    # self.ssb_lineEdit.setGeometry(1180, 5, 165, 25)
    # self.ssb_pushButton_01.setGeometry(1010, 35, 165, 30)
    # self.ssb_pushButton_02.setGeometry(1180, 35, 165, 30)
    # self.ssb_pushButton_03.setGeometry(1010, 70, 165, 30)
    # self.ssb_pushButton_04.setGeometry(1180, 70, 165, 30)
    # self.ssb_pushButton_05.setGeometry(1010, 105, 165, 30)
    # self.ssb_pushButton_06.setGeometry(1180, 105, 165, 30)
    # self.ssb_pushButton_07.setGeometry(1010, 140, 165, 30)
    # self.ssb_pushButton_08.setGeometry(1180, 140, 165, 30)
    # self.ssb_pushButton_09.setGeometry(1010, 175, 165, 30)
    # self.ssb_pushButton_10.setGeometry(1180, 175, 165, 30)
    # self.ssb_pushButton_11.setGeometry(1010, 210, 165, 30)
    # self.ssb_pushButton_12.setGeometry(1180, 210, 165, 30)
    # self.ssb_pushButton_13.setGeometry(1010, 245, 165, 30)
    # self.ssb_pushButton_14.setGeometry(1180, 245, 165, 30)
    # self.ssb_pushButton_15.setGeometry(1010, 280, 165, 30)
    # self.ssb_pushButton_16.setGeometry(1180, 280, 165, 30)

    # self.ssb_labellll_01.setGeometry(1010, 320, 335, 20)
    # self.ssb_labellll_02.setGeometry(1010, 345, 335, 20)
    # self.ssb_labellll_03.setGeometry(1010, 370, 335, 20)

    # self.ssb_dateEdit_01.setGeometry(1110, 320, 110, 20)
    # self.ssb_dateEdit_02.setGeometry(1235, 320, 110, 20)
    # self.ssb_lineEdit_01.setGeometry(1175, 345, 55, 20)
    # self.ssb_lineEdit_02.setGeometry(1290, 345, 55, 20)
    # self.ssb_lineEdit_03.setGeometry(1065, 370, 55, 20)
    # self.ssb_lineEdit_04.setGeometry(1175, 370, 55, 20)
    # self.ssb_lineEdit_05.setGeometry(1290, 370, 55, 20)
    # self.sb_pushButton_01.setGeometry(1010, 400, 165, 30)
    # self.sb_pushButton_02.setGeometry(1180, 400, 165, 30)
    # self.sb_pushButton_03.setGeometry(1010, 435, 165, 30)
    # self.sb_pushButton_04.setGeometry(1180, 435, 165, 30)

    # self.sss_comboBox.setGeometry(1010, 473, 165, 25)
    # self.sss_lineEdit.setGeometry(1180, 473, 165, 25)
    # self.sss_pushButton_01.setGeometry(1010, 503, 165, 30)
    # self.sss_pushButton_02.setGeometry(1180, 503, 165, 30)
    # self.sss_pushButton_03.setGeometry(1010, 538, 165, 30)
    # self.sss_pushButton_04.setGeometry(1180, 538, 165, 30)
    # self.sss_pushButton_05.setGeometry(1010, 573, 165, 30)
    # self.sss_pushButton_06.setGeometry(1180, 573, 165, 30)
    # self.sss_pushButton_07.setGeometry(1010, 608, 165, 30)
    # self.sss_pushButton_08.setGeometry(1180, 608, 165, 30)
    # self.sss_pushButton_09.setGeometry(1010, 643, 165, 30)
    # self.sss_pushButton_10.setGeometry(1180, 643, 165, 30)
    # self.sss_pushButton_11.setGeometry(1010, 678, 165, 30)
    # self.sss_pushButton_12.setGeometry(1180, 678, 165, 30)
    # self.sss_pushButton_13.setGeometry(1010, 713, 165, 30)
    # self.sss_pushButton_14.setGeometry(1180, 713, 165, 30)

    # self.cs_textEdit_01.setGeometry(5, 5, 1000, 463)
    # self.cs_textEdit_02.setGeometry(5, 473, 1000, 270)
    # self.cs_textEdit_03.setGeometry(5, 5, 1000, 738)

    # self.csb_comboBox.setGeometry(1010, 5, 165, 25)
    # self.csb_lineEdit.setGeometry(1180, 5, 165, 25)
    # self.csb_pushButton_01.setGeometry(1010, 35, 165, 30)
    # self.csb_pushButton_02.setGeometry(1180, 35, 165, 30)
    # self.csb_pushButton_03.setGeometry(1010, 70, 165, 30)
    # self.csb_pushButton_04.setGeometry(1180, 70, 165, 30)
    # self.csb_pushButton_05.setGeometry(1010, 105, 165, 30)
    # self.csb_pushButton_06.setGeometry(1180, 105, 165, 30)
    # self.csb_pushButton_07.setGeometry(1010, 140, 165, 30)
    # self.csb_pushButton_08.setGeometry(1180, 140, 165, 30)
    # self.csb_pushButton_09.setGeometry(1010, 175, 165, 30)
    # self.csb_pushButton_10.setGeometry(1180, 175, 165, 30)
    # self.csb_pushButton_11.setGeometry(1010, 210, 165, 30)
    # self.csb_pushButton_12.setGeometry(1180, 210, 165, 30)
    # self.csb_pushButton_13.setGeometry(1010, 245, 165, 30)
    # self.csb_pushButton_14.setGeometry(1180, 245, 165, 30)
    # self.csb_pushButton_15.setGeometry(1010, 280, 165, 30)
    # self.csb_pushButton_16.setGeometry(1180, 280, 165, 30)

    # self.csb_labellll_01.setGeometry(1010, 320, 335, 20)
    # self.csb_labellll_02.setGeometry(1010, 345, 335, 20)
    # self.csb_labellll_03.setGeometry(1010, 370, 335, 20)

    # self.csb_dateEdit_01.setGeometry(1110, 320, 110, 20)
    # self.csb_dateEdit_02.setGeometry(1235, 320, 110, 20)
    # self.csb_lineEdit_01.setGeometry(1175, 345, 55, 20)
    # self.csb_lineEdit_02.setGeometry(1290, 345, 55, 20)
    # self.csb_lineEdit_03.setGeometry(1065, 370, 55, 20)
    # self.csb_lineEdit_04.setGeometry(1175, 370, 55, 20)
    # self.csb_lineEdit_05.setGeometry(1290, 370, 55, 20)
    # self.cb_pushButton_01.setGeometry(1010, 400, 165, 30)
    # self.cb_pushButton_02.setGeometry(1180, 400, 165, 30)
    # self.cb_pushButton_03.setGeometry(1010, 435, 165, 30)
    # self.cb_pushButton_04.setGeometry(1180, 435, 165, 30)

    # self.css_comboBox.setGeometry(1010, 473, 165, 25)
    # self.css_lineEdit.setGeometry(1180, 473, 165, 25)
    # self.css_pushButton_01.setGeometry(1010, 503, 165, 30)
    # self.css_pushButton_02.setGeometry(1180, 503, 165, 30)
    # self.css_pushButton_03.setGeometry(1010, 538, 165, 30)
    # self.css_pushButton_04.setGeometry(1180, 538, 165, 30)
    # self.css_pushButton_05.setGeometry(1010, 573, 165, 30)
    # self.css_pushButton_06.setGeometry(1180, 573, 165, 30)
    # self.css_pushButton_07.setGeometry(1010, 608, 165, 30)
    # self.css_pushButton_08.setGeometry(1180, 608, 165, 30)
    # self.css_pushButton_09.setGeometry(1010, 643, 165, 30)
    # self.css_pushButton_10.setGeometry(1180, 643, 165, 30)
    # self.css_pushButton_11.setGeometry(1010, 678, 165, 30)
    # self.css_pushButton_12.setGeometry(1180, 678, 165, 30)
    # self.css_pushButton_13.setGeometry(1010, 713, 165, 30)
    # self.css_pushButton_14.setGeometry(1180, 713, 165, 30)



    # self.sj_main_comboBox_01.setGeometry(10, 30, 140, 22)
    # self.sj_main_checkBox_01.setGeometry(170, 30, 90, 20)
    # self.sj_main_checkBox_02.setGeometry(270, 30, 90, 20)
    # self.sj_main_checkBox_03.setGeometry(370, 30, 90, 20)

    # self.sj_main_comboBox_02.setGeometry(500, 30, 140, 22)
    # self.sj_main_checkBox_04.setGeometry(660, 30, 90, 20)
    # self.sj_main_checkBox_05.setGeometry(760, 30, 90, 20)
    # self.sj_main_checkBox_06.setGeometry(860, 30, 90, 20)

    # self.sj_main_labellll_01.setGeometry(10, 60, 1000, 20)
    # self.sj_main_lineEdit_01.setGeometry(200, 60, 50, 20)
    # self.sj_main_lineEdit_02.setGeometry(410, 60, 50, 20)
    # self.sj_main_lineEdit_03.setGeometry(690, 60, 50, 20)
    # self.sj_main_lineEdit_04.setGeometry(900, 60, 50, 20)

    # self.sj_main_checkBox_07.setGeometry(10, 90, 160, 20)
    # self.sj_main_checkBox_08.setGeometry(180, 90, 125, 20)
    # self.sj_main_labellll_03.setGeometry(295, 90, 105, 20)
    # self.sj_main_lineEdit_05.setGeometry(410, 90, 50, 20)

    # self.sj_main_checkBox_09.setGeometry(500, 90, 160, 20)
    # self.sj_main_checkBox_10.setGeometry(670, 90, 125, 20)
    # self.sj_main_labellll_04.setGeometry(785, 90, 105, 20)
    # self.sj_main_lineEdit_06.setGeometry(900, 90, 50, 20)

    # self.sj_sacc_labellll_01.setGeometry(10, 30, 1000, 20)
    # self.sj_sacc_lineEdit_01.setGeometry(115, 30, 130, 20)
    # self.sj_sacc_lineEdit_02.setGeometry(330, 30, 130, 20)
    # self.sj_sacc_lineEdit_03.setGeometry(585, 30, 130, 20)
    # self.sj_sacc_lineEdit_04.setGeometry(820, 30, 130, 20)
    # self.sj_sacc_labellll_02.setGeometry(10, 60, 1000, 20)
    # self.sj_sacc_lineEdit_05.setGeometry(115, 60, 130, 20)
    # self.sj_sacc_lineEdit_06.setGeometry(330, 60, 130, 20)
    # self.sj_sacc_lineEdit_07.setGeometry(585, 60, 130, 20)
    # self.sj_sacc_lineEdit_08.setGeometry(820, 60, 130, 20)

    # self.sj_cacc_labellll_01.setGeometry(10, 30, 1000, 20)
    # self.sj_cacc_lineEdit_01.setGeometry(85, 30, 375, 20)
    # self.sj_cacc_lineEdit_02.setGeometry(575, 30, 375, 20)

    # self.sj_tele_labellll_01.setGeometry(10, 30, 1000, 20)
    # self.sj_tele_lineEdit_01.setGeometry(85, 30, 375, 20)
    # self.sj_tele_lineEdit_02.setGeometry(575, 30, 375, 20)

    # self.sj_stock_checkBox_01.setGeometry(10, 30, 90, 20)
    # self.sj_stock_checkBox_02.setGeometry(10, 60, 90, 20)

    # self.sj_stock_labellll_01.setGeometry(100, 30, 910, 20)
    # self.sj_stock_comboBox_01.setGeometry(175, 30, 125, 22)
    # self.sj_stock_comboBox_02.setGeometry(335, 30, 125, 22)
    # self.sj_stock_lineEdit_01.setGeometry(580, 30, 50, 20)
    # self.sj_stock_lineEdit_02.setGeometry(725, 30, 50, 20)
    # self.sj_stock_labellll_02.setGeometry(100, 60, 910, 20)
    # self.sj_stock_comboBox_03.setGeometry(175, 60, 125, 22)
    # self.sj_stock_comboBox_04.setGeometry(335, 60, 125, 22)
    # self.sj_stock_lineEdit_03.setGeometry(580, 60, 50, 20)
    # self.sj_stock_lineEdit_04.setGeometry(725, 60, 50, 20)

    # self.sj_coin_checkBox_01.setGeometry(10, 30, 90, 20)
    # self.sj_coin_checkBox_02.setGeometry(10, 60, 90, 20)

    # self.sj_coin_labellll_01.setGeometry(100, 30, 910, 20)
    # self.sj_coin_comboBox_01.setGeometry(175, 30, 125, 22)
    # self.sj_coin_comboBox_02.setGeometry(335, 30, 125, 22)
    # self.sj_coin_lineEdit_01.setGeometry(580, 30, 50, 20)
    # self.sj_coin_lineEdit_02.setGeometry(725, 30, 50, 20)
    # self.sj_coin_labellll_02.setGeometry(100, 60, 910, 20)
    # self.sj_coin_comboBox_03.setGeometry(175, 60, 125, 22)
    # self.sj_coin_comboBox_04.setGeometry(335, 60, 125, 22)
    # self.sj_coin_lineEdit_03.setGeometry(580, 60, 50, 20)
    # self.sj_coin_lineEdit_04.setGeometry(725, 60, 50, 20)

    # self.sj_load_pushButton_00.setGeometry(1180, 60, 150, 22)
    # self.sj_load_pushButton_01.setGeometry(1180, 30, 70, 22)
    # self.sj_load_pushButton_02.setGeometry(1180, 30, 70, 22)
    # self.sj_load_pushButton_03.setGeometry(1180, 30, 70, 22)
    # self.sj_load_pushButton_04.setGeometry(1180, 30, 70, 22)
    # self.sj_load_pushButton_05.setGeometry(1180, 30, 70, 22)
    # self.sj_load_pushButton_06.setGeometry(1180, 30, 70, 22)

    # self.sj_save_pushButton_01.setGeometry(1260, 30, 70, 22)
    # self.sj_save_pushButton_02.setGeometry(1260, 30, 70, 22)
    # self.sj_save_pushButton_03.setGeometry(1260, 30, 70, 22)
    # self.sj_save_pushButton_04.setGeometry(1260, 30, 70, 22)
    # self.sj_save_pushButton_05.setGeometry(1260, 30, 70, 22)
    # self.sj_save_pushButton_06.setGeometry(1260, 30, 70, 22)

    # self.dialog_chart.setFixedSize(760, 1000)
    # self.ct_groupBox_01.setGeometry(5, -10, 750, 62)
    # self.ct_groupBox_02.setGeometry(5, 40, 750, 955)

    # self.ct_dateEdit.setGeometry(10, 25, 160, 30)
    # self.ct_labellll_01.setGeometry(190, 25, 90, 30)
    # self.ct_lineEdit_01.setGeometry(290, 25, 80, 30)
    # self.ct_labellll_02.setGeometry(390, 25, 120, 30)
    # self.ct_lineEdit_02.setGeometry(520, 25, 120, 30)
    # self.ct_pushButton_01.setGeometry(650, 25, 95, 30)

    # self.ct_labellll_03.setGeometry(20, 40, 200, 15)
    # self.ct_labellll_04.setGeometry(20, 345, 200, 15)
    # self.ct_labellll_05.setGeometry(20, 650, 200, 15)

    # self.ct_labellll_06.setGeometry(20, 65, 200, 15)
    # self.ct_labellll_07.setGeometry(20, 375, 200, 40)
    # self.ct_labellll_08.setGeometry(20, 680, 200, 25)

    # self.dialog_hoga.setFixedSize(572, 355)
    # self.hj_tableWidget.setGeometry(5, 5, 562, 42)
    # self.hc_tableWidget.setGeometry(5, 52, 282, 297)
    # self.hg_tableWidget.setGeometry(285, 52, 282, 297)
    # self.hg_line.setGeometry(5, 209, 562, 1)

    

    