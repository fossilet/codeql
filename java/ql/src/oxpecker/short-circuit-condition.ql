/**
 * @name short-circuit-condition-bypass
 * @description short-circuit condition bypass
 * @kind problem
 * @problem.severity recommendation
 * @precision medium
 * @id java/short-circuit-bypass
 * @tags security
 */
class ValidationFunction extends Method {
  ValidationFunction() {
    exists(string n | n = this.getName() | n.matches("verify%") or n.matches("check%"))
  }

  predicate isSecureByDefault() { this.getBody().getLastStmt() instanceof PosReturn }
}

string toString(Expr st) {
  if exists(st.getAChildExpr())
  then result = st.toString() + "(" + toString(st.getAChildExpr()) + ")"
  else result = "(" + st.toString() + ")"
}

predicate isPosResult(Expr expr) {
  exists(string ret | ret = toString(expr) |
    ret.matches("%(true)%") or ret.matches("%(ok)%") or ret.matches("%(suc%")
  )
}

predicate isNegResult(Expr expr) {
  exists(string ret | ret = toString(expr) |
    ret.matches("%(false)%") or ret.matches("%(err%") or ret.matches("%(fail%")
  )
}

Stmt nearestNonIfStmt(Stmt stmt) {
  if stmt.getParent() instanceof IfStmt
  then result = stmt
  else result = nearestNonIfStmt(stmt.getParent())
}

class PosReturn extends ReturnStmt {
  PosReturn() { isPosResult(this.getResult()) }
}

class NegReturn extends ReturnStmt {
  NegReturn() { isNegResult(this.getResult()) }
}

class IfAnd extends IfStmt {
  IfAnd() { this.getCondition() instanceof AndLogicalExpr }
}

import java

from IfAnd ifa, NegReturn nr, ValidationFunction vf, Element origin
where
  origin = vf and
  ifa.getThen() = nearestNonIfStmt(nr) and
  ifa.getEnclosingCallable() = vf and
  vf.isSecureByDefault()
select vf.getDeclaringType(), "short-circuit condition bypass", vf, vf.getName(),
  ifa.getCondition().(AndLogicalExpr).getRightOperand(), "supressed",
  ifa.getCondition().(AndLogicalExpr).getLeftOperand(), "by"
